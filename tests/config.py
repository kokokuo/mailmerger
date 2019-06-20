

class TestConifg(object):
    LOGGER_NAME = "testing-logger"

    SHEET_TEST_DIRNAME = "sheets"
    EMAIL_TEMPLATE_TEST_DIRNAME = "templates"

    TEST01_EN_HEADER_SHEET_FILENAME = "Test01-EN-Header.xlsx"
    TEST01_EN_HEADER_SHEET_NAME = "HotelsInfo"
    TEST01_EN_HEADER_NON_EXIST_SHEET_NAME = "Sheet1"

    TEST02_CN_HEADER_SHEET_FILENAME = "Test02-CN-Header.xlsx"
    TEST03_NON_EXIST_SHEET_FILENAME = "NotExistSheetFile.xlsx"

    TEST04_NON_EXCEL_FORMAT_FILE = "Test04-FileNotExcelFormat.txt"

    TEST01_EN_HEADER_SHEET_EXPECTED_RESULT = [
        {
            "HotelName": "台北君悅酒店",
            "Address": "110臺北市信義區松壽路2號",
            "Phone": "02-2720-1234",
            "TotalRooms": 865,
            "WebsiteUrl": "http://taipei.grand.hyatt.com",
            "Email": "taipei.grand@hyatt.com"
        },
        {
            "HotelName": "凱達大飯店",
            "Address": "108臺北市萬華區艋舺大道167號",
            "Phone": "02-2306-6777",
            "TotalRooms": 745,
            "WebsiteUrl": "http://www.caesarmetro.com",
            "Email": "cm.reservation@caesarpark.com.tw"
        },
        {
            "HotelName": "王朝大酒店",
            "Address": "105臺北市松山區敦化北路100號",
            "Phone": "02-27198399",
            "TotalRooms": 713,
            "WebsiteUrl": "http://www.sunworlddynasty.com.tw",
            "Email": "bc@sunworlddynasty.com.tw",
        },
    ]

    TEST02_CN_HEADER_SHEET_EXPECTED_RESULT = [
        {
            "旅館名稱": "台北君悅酒店",
            "地址": "110臺北市信義區松壽路2號",
            "聯絡電話": "02-2720-1234",
            "總房間數": 865,
            "網址": "http://taipei.grand.hyatt.com",
            "信箱": "taipei.grand@hyatt.com"
        },
        {
            "旅館名稱": "凱達大飯店",
            "地址": "108臺北市萬華區艋舺大道167號",
            "聯絡電話": "02-2306-6777",
            "總房間數": 745,
            "網址": "http://www.caesarmetro.com",
            "信箱": "cm.reservation@caesarpark.com.tw"
        },
        {
            "旅館名稱": "王朝大酒店",
            "地址": "105臺北市松山區敦化北路100號",
            "聯絡電話": "02-27198399",
            "總房間數": 713,
            "網址": "http://www.sunworlddynasty.com.tw",
            "信箱": "bc@sunworlddynasty.com.tw",
        }
    ]

    TEST02_CN_HEADER_SHEET_NON_EXPECTED_RESULT = [
        {
            "旅館名稱": "台北君悅酒店",
            "地址": "110臺北市信義區松壽路2號",
            "聯絡電話": "02-2720-1234",
            "總房間數": 865,
            "網址": "http://taipei.grand.hyatt.com",
            "信箱": "taipei.grand@hyatt.com"
        },
        {
            "旅館名稱": "凱達大飯店",
            "地址": "108臺北市萬華區艋舺大道167號",
            "聯絡電話": "02-2306-6777",
            "總房間數": 713,
            "網址": "http://www.caesarmetro.com",
            "信箱": "bc@sunworlddynasty.com.tw",
        },
        {
            "旅館名稱": "王朝大酒店",
            "地址": "105臺北市松山區敦化北路100號",
            "聯絡電話": "02-27198399",
            "總房間數": 745,
            "網址": "http://www.sunworlddynasty.com.tw",
            "信箱": "cm.reservation@caesarpark.com.tw"
        }
    ]




