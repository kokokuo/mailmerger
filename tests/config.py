from enum import Enum


class TestCommonConifg(object):
    LOGGER_NAME = "testing-logger"
    SHEET_TEST_DIRNAME = "sheets"
    EMAIL_TEMPLATE_TEST_DIRNAME = "templates"


class TestSheetColHeader(Enum):
    """
    TestEnHeader.xlsx 與 TestCnHeader.xlsx 的 Coulmn 標頭定義，差異為英文跟中文
    """
    EN_HOTELNAME = "HotelName"
    EN_ADDRESS = "Address"
    EN_PHONE = "Phone"
    EN_TOTAL_ROOMS = "TotalRooms"
    EN_WEBSITE_URL = "WebsiteUrl"
    EN_EMAIL = "Email"

    CN_HOTELNAME = "旅館名稱"
    CN_ADDRESS = "地址"
    CN_PHONE = "聯絡電話"
    CN_TOTAL_ROOMS = "總房間數"
    CN_WEBSITE_URL = "網址"
    CN_EMAIL = "信箱"


class TestSheetConifg(object):
    TEST_EN_HEADER_SHEET_FILENAME = "TestEnHeader.xlsx"
    TEST_CN_HEADER_SHEET_FILENAME = "TestCnHeader.xlsx"
    TEST_NON_EXIST_SHEET_FILENAME = "NotExistSheetFile.xlsx"
    TEST_NON_EXCEL_FORMAT_FILE = "TestFileNotExcelFormat.txt"

    """
    檔案的試算表名稱
    """
    TEST_EN_HEADER_SHEET_NAME = "HotelsInfo"
    TEST_EN_HEADER_NON_EXIST_SHEET_NAME = "sheet1"

    TEST_CN_HEADER_NON_EXIST_SHEET_NAME = "試算表"
    TEST_CN_HEADER_SHEET_NAME = "旅館資訊"


class TestParsinExcelSheetConifg(object):
    """
    TestEnHeader.xlsx 每 Row 資料：與 TestCnHeader.xlsx 的差異在 Column 標頭定義為英文
    """
    TEST_DATASHEET_EN_HEADER_ROW_A = {
        TestSheetColHeader.EN_HOTELNAME.value: "台北君悅酒店",
        TestSheetColHeader.EN_ADDRESS.value: "110臺北市信義區松壽路2號",
        TestSheetColHeader.EN_PHONE.value: "02-2720-1234",
        TestSheetColHeader.EN_TOTAL_ROOMS.value: 865,
        TestSheetColHeader.EN_WEBSITE_URL.value: "http://taipei.grand.hyatt.com",
        TestSheetColHeader.EN_EMAIL.value: "taipei.grand@hyatt.com"
    }
    TSET_DATASHEET_EN_HEADER_ROW_B = {
        TestSheetColHeader.EN_HOTELNAME.value: "凱達大飯店",
        TestSheetColHeader.EN_ADDRESS.value: "108臺北市萬華區艋舺大道167號",
        TestSheetColHeader.EN_PHONE.value: "02-2306-6777",
        TestSheetColHeader.EN_TOTAL_ROOMS.value: 745,
        TestSheetColHeader.EN_WEBSITE_URL.value: "http://www.caesarmetro.com",
        TestSheetColHeader.EN_EMAIL.value: "cm.reservation@caesarpark.com.tw"
    }

    TSET_DATASHEET_EN_HEADER_ROW_C = {
        TestSheetColHeader.EN_HOTELNAME.value: "王朝大酒店",
        TestSheetColHeader.EN_ADDRESS.value: "105臺北市松山區敦化北路100號",
        TestSheetColHeader.EN_PHONE.value: "02-27198399",
        TestSheetColHeader.EN_TOTAL_ROOMS.value: 713,
        TestSheetColHeader.EN_WEBSITE_URL.value: "http://www.sunworlddynasty.com.tw",
        TestSheetColHeader.EN_EMAIL.value: "bc@sunworlddynasty.com.tw",
    }

    """
    TestCnHeader.xlsx 每 Row 資料：Column 標頭定義中文
    """
    TEST_DATASHEET_CN_HEADER_ROW_A = {
        TestSheetColHeader.CN_HOTELNAME.value: "台北君悅酒店",
        TestSheetColHeader.CN_ADDRESS.value: "110臺北市信義區松壽路2號",
        TestSheetColHeader.CN_PHONE.value: "02-2720-1234",
        TestSheetColHeader.CN_TOTAL_ROOMS.value: 865,
        TestSheetColHeader.CN_WEBSITE_URL.value: "http://taipei.grand.hyatt.com",
        TestSheetColHeader.CN_EMAIL.value: "taipei.grand@hyatt.com"
    }
    TSET_DATASHEET_CN_HEADER_ROW_B = {
        TestSheetColHeader.CN_HOTELNAME.value: "凱達大飯店",
        TestSheetColHeader.CN_ADDRESS.value: "108臺北市萬華區艋舺大道167號",
        TestSheetColHeader.CN_PHONE.value: "02-2306-6777",
        TestSheetColHeader.CN_TOTAL_ROOMS.value: 745,
        TestSheetColHeader.CN_WEBSITE_URL.value: "http://www.caesarmetro.com",
        TestSheetColHeader.CN_EMAIL.value: "cm.reservation@caesarpark.com.tw"
    }

    TSET_DATASHEET_CN_HEADER_ROW_C = {
        TestSheetColHeader.CN_HOTELNAME.value: "王朝大酒店",
        TestSheetColHeader.CN_ADDRESS.value: "105臺北市松山區敦化北路100號",
        TestSheetColHeader.CN_PHONE.value: "02-27198399",
        TestSheetColHeader.CN_TOTAL_ROOMS.value: 713,
        TestSheetColHeader.CN_WEBSITE_URL.value: "http://www.sunworlddynasty.com.tw",
        TestSheetColHeader.CN_EMAIL.value: "bc@sunworlddynasty.com.tw",
    }

    """
    TestCnHeader.xlsx 的第四筆資料，作為測試錯誤的預期結果使用
    """
    TSET_DATASHEET_CN_HEADER_ROW_D = {
        TestSheetColHeader.CN_HOTELNAME.value: "台北寒舍喜來登大飯店",
        TestSheetColHeader.CN_ADDRESS.value: "100臺北市中正區忠孝東路1段12號",
        TestSheetColHeader.CN_PHONE.value: "02-2321-5511",
        TestSheetColHeader.CN_TOTAL_ROOMS.value: 692,
        TestSheetColHeader.CN_WEBSITE_URL.value: "http://www.sheratongrandtaipei.com",
        TestSheetColHeader.CN_EMAIL.value: "sheraton@sheratongrandtaipei.com",
    }

    """
    TestEnHeader.xlsx 與 TestCnHeader.xlsx 的預期正確測試資料
    """
    TEST_EN_HEADER_SHEET_EXPECTED_RESULT = [
        TEST_DATASHEET_EN_HEADER_ROW_A,
        TSET_DATASHEET_EN_HEADER_ROW_B,
        TSET_DATASHEET_EN_HEADER_ROW_C
    ]

    TEST_CN_HEADER_SHEET_EXPECTED_RESULT = [
        TEST_DATASHEET_CN_HEADER_ROW_A,
        TSET_DATASHEET_CN_HEADER_ROW_B,
        TSET_DATASHEET_CN_HEADER_ROW_C
    ]

    """
    TestCnHeader.xlsx 的預期錯誤測試，分別為資料不同 與 順序不同
    """
    TEST_CN_HEADER_SHEET_NON_EXPECTED_RESULT_DATA_DIFF = [
        TEST_DATASHEET_CN_HEADER_ROW_A,
        TSET_DATASHEET_CN_HEADER_ROW_C,
        TSET_DATASHEET_CN_HEADER_ROW_B
    ]

    TEST_CN_HEADER_SHEET_NON_EXPECTED_RESULT_ORDER_DIFF = [
        TEST_DATASHEET_CN_HEADER_ROW_A,
        TSET_DATASHEET_CN_HEADER_ROW_B,
        TSET_DATASHEET_CN_HEADER_ROW_D
    ]


class TestParsingSourceConifg(object):

    """
    預期的合併 Column 標頭 以及資料
    """
    TEST_CH_PREMERGE_SOURCE_EXPECTED_COLHEADER = [
        TestSheetColHeader.CN_HOTELNAME.value,
        TestSheetColHeader.CN_ADDRESS.value,
        TestSheetColHeader.CN_PHONE.value,
        TestSheetColHeader.CN_TOTAL_ROOMS.value,
        TestSheetColHeader.CN_WEBSITE_URL.value,
        TestSheetColHeader.CN_EMAIL.value
    ]

    TEST_CH_PREMERGE_SOURCE_EXPECTED_ROWSET = \
        TestParsinExcelSheetConifg.TEST_CN_HEADER_SHEET_EXPECTED_RESULT

    """
    預期錯誤的合併 Column 標頭 以及 資料 - 資料不正確
    """
    TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_DATA_DIFF = [
        TestSheetColHeader.EN_HOTELNAME.value,
        TestSheetColHeader.CN_ADDRESS.value,
        TestSheetColHeader.CN_PHONE.value,
        TestSheetColHeader.CN_TOTAL_ROOMS.value,
        TestSheetColHeader.CN_WEBSITE_URL.value,
        TestSheetColHeader.EN_EMAIL.value
    ]
    TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_ROWSET_DATA_DIFF = \
        TestParsinExcelSheetConifg.TEST_CN_HEADER_SHEET_NON_EXPECTED_RESULT_DATA_DIFF

    """
    預期錯誤的合併 Column 標頭 以及 資料 - 順序不正確
    """
    TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_COLHEADER_ORDER_DIFF = [
        TestSheetColHeader.CN_HOTELNAME.value,
        TestSheetColHeader.CN_TOTAL_ROOMS.value,
        TestSheetColHeader.CN_PHONE.value,
        TestSheetColHeader.CN_WEBSITE_URL.value,
        TestSheetColHeader.CN_EMAIL.value,
        TestSheetColHeader.CN_ADDRESS.value
    ]
    TEST_CH_PREMERGE_SOURCE_NON_EXPECTED_ROWSET_ORDER_DIFF = \
        TestParsinExcelSheetConifg.TEST_CN_HEADER_SHEET_NON_EXPECTED_RESULT_ORDER_DIFF
