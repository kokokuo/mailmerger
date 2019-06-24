# -*- coding: utf-8 -*-
import os
import math
import smtplib
import json
from jinja2 import Environment, PackageLoader, select_autoescape, meta, TemplateNotFound
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailAgent(object):
    def __init__(self, mail_name):
        """
        Args:
            mail_name(str): 信件的樣本檔案名稱
        """
        self._jinja_env = Environment(
            loader=PackageLoader("app", "templates"),
            autoescape=select_autoescape(["html", "xml"])
        )
        self._mail_name = mail_name
        self._mail_content_template = None
        self._config_json =  \
            json.loads(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r").read())

    def __find_variables(self, env, mail_name):
        """
        找到放在 template 中的 variable
        """
        try:
            template_source = env.loader.get_source(env, mail_name)[0]
            parsed_content = env.parse(template_source)
            vars = meta.find_undeclared_variables(parsed_content)
            return vars
        except TemplateNotFound as te:
            print("該檔案找不到....")

    def __mapping_variable(self, template_vars, mapping_data):
        # 找出要比對的關鍵字有哪些不存在於信件樣版
        # 全部變成 utf8格式對應
        template_vars = set([var.decode("utf8") for var in template_vars])
        not_include_template_vars = set(mapping_data.keys()) - template_vars
        # 哪些樣板的資料沒被比對到
        not_mapped_var_in_template = template_vars - set(mapping_data.keys())
        if not_include_template_vars:
            print("此筆資料中的欄位: {}, 不存在於信件樣板中，因此無法被匹配填入".format(", ".join(not_include_template_vars)))
        if not_mapped_var_in_template:
            print("信件中的替換關鍵字 {} 沒有資料對應到".format(", ".join(not_mapped_var_in_template)))
        # if raw_input("如果要繼續寄信，請按任意鍵，否則按 q 停此寄送此封 >>> ") == "q":
        # 	return False
        return True

    def send_mapped_data_email(self, mapping_data):
        """
        寄送替換關鍵字的信件
        Args:
            mapping_data（dict): 要兌換信件關鍵字匹配的資料
        """

        template_vars = self.__find_variables(self._jinja_env, self._mail_name)
        if self.__mapping_variable(template_vars, mapping_data):
            html_content = self._jinja_env.get_template(self._mail_name).render(**mapping_data)
            sender = self._config_json["sender_mail"]
            sender_name = self._config_json["sender_name"]
            receivers = self._config_json["test"]["receiver"]
            # 信件準備
            msg_root = MIMEMultipart("related")
            msg_root["Subject"] = self._config_json["mail_subject"]
            msg_root["From"] = sender_name
            if "email" in mapping_data.keys() and (type(mapping_data["email"]) is str):
                receivers = [mapping_data["email"]]
                # receivers = ["v6610688@gmail.com"]
                msg_root["To"] = ",".join(receivers)
            else:
                print("民宿：", mapping_data["hotel_name"], "「不存在信箱...繼續下一封」")
                print("==================================s================================")
                return
            msg_alternative = MIMEMultipart("alternative")
            msg_root.attach(msg_alternative)
            msg_alternative.attach(MIMEText(html_content, "html", "utf-8"))
            try:
                smtp_obj = smtplib.SMTP(self._config_json["smtp_host"], 587)
                smtp_obj.ehlo()
                smtp_obj.starttls()
                smtp_obj.login(sender, self._config_json["password"])
                smtp_obj.sendmail(sender, receivers, msg_root.as_string())
                print("民宿：", mapping_data["hotel_name"], "「Done, 郵件發送成功！」")
                print("==================================================================")
            except smtplib.SMTPException:
                print("Error", "民宿：", mapping_data["hotel_name"], "「無法發送郵件.......」")
                return
