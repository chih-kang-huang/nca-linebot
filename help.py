#from linebot import (
#    LineBotApi, WebhookHandler)
import order_lib
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
#    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
#    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
#    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
#    ImageMessage, VideoMessage, AudioMessage, FileMessage,
#    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
#    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
#    TextComponent, IconComponent, ButtonComponent,
#    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)

#carouselButton = [
#    CarouselColumn(
#        title='點擊',
#        text=' ',
#        actions=[
#            MessageAction(
#                label='取消',
#                text='取消/'
#            ),
#            MessageAction(
#                label='統計',
#                text='統計/'
#            ),
#            MessageAction(
#                label='清除',
#                text='清除/'
#            )
#        ]
#    
#    )
#]
#def helpWithCarousel():
#    """ Return help message text with carousel template 
#    If there is an image, there have to be images at every cols
#    """
#    carousel_template = CarouselTemplate(columns=[
#        CarouselColumn(#thumbnail_image_url='https://imgur.com/gallery/p2DNWk3',
#                       title='指令', 
#                       text='試試看這個範例！', 
#                       actions=[
#                           MessageAction(label='範例說明', 
#                           text='指令輸入格式：[指令]/[內容1]/[內容2]...\n\
#                           餐廳範例： 點/13/5/3/2\n\
#                           飲料範例： 喝/3,L,無糖少冰/12,M,全糖/6,中杯,半糖多冰\n\
#                           取消範例： 取消/\n\
#                                         指令：說明、吃、點、取消、統計、截止、清除')
#        ])
#        ,
#        CarouselColumn(#thumbnail_image_url='https://imgur.com/gallery/p2DNWk3',
#                       title='來源', 
#                       text='請查看：', 
#                       actions=[
#                           URIAction(label='GitHub Repo', uri='https://github.com/CheesyPicodon/ncu-line-bot')
#        ])
#        ,
#        CarouselColumn(#thumbnail_image_url='https://imgur.com/gallery/p2DNWk3',
#                       title='取消', 
#                       text='取消點餐', 
#                       actions=[
#                           MessageAction(label='取消', 
#                           text='取消/')
#        ])
#        ,
#        CarouselColumn(#thumbnail_image_url='https://imgur.com/gallery/p2DNWk3',
#                       title='點餐1-3', 
#                       text='點1-3', 
#                       actions=[
#                           MessageAction(
#                               label='2', 
#                               text='點/2'
#                           )
#        ]),
#        CarouselColumn(
#            title='',
#            text='',
#            actions=[
#                 PostbackAction(
#                        label='postback1',
#                        display_text='postback text1',
#                        data='action=buy&itemid=1'
#                 ),
#                MessageAction(
#                        label='',
#                        text='點/23'
#                    ),
#                URIAction(
#                        label='uri1',
#                        uri='http://example.com/1'
#                    )
#        
#    ])
#    return TemplateSendMessage(alt_text='Carousel alt text', template=carousel_template)

def helpWithCarousel():
    """ Return help message text with carousel template 
    If there is an image, there have to be images at every cols
    """
    carousel_template = CarouselTemplate(columns=[
        CarouselColumn(
            title='點擊',
            text=' ',
            actions=[
                MessageAction(
                    label='取消',
                    text='取消/'
                ),
                MessageAction(
                    label='統計',
                    text='統計/'
                ),
                MessageAction(
                    label='清除',
                    text='清除/'
                )
            ]
        
        ),
        CarouselColumn(
            title='1-3',
            text='1-3',
            actions=[
                MessageAction(
                    label='1',
                    text='點/1'
                ),
                MessageAction(
                    label='2',
                    text='點/2'
                ),
                MessageAction(
                    label='3',
                    text='點/3'
                )
            ]
        
        ),
        CarouselColumn(
            title='4-6',
            text='4-6',
            actions=[
                MessageAction(
                    label='4',
                    text='點/4'
                ),
                MessageAction(
                    label='5',
                    text='點/5'
                ),
                MessageAction(
                    label='6',
                    text='點/6'
                )
            ]
        
        ),
        CarouselColumn(
            title='7-9',
            text='7-9',
            actions=[
                MessageAction(
                    label='7',
                    text='點/7'
                ),
                MessageAction(
                    label='8',
                    text='點/8'
                ),
                MessageAction(
                    label='9',
                    text='點/9'
                )
            ]
        
        ),
        CarouselColumn(
            title='10-12',
            text='10-12',
            actions=[
                MessageAction(
                    label='10',
                    text='點/10'
                ),
                MessageAction(
                    label='11',
                    text='點/11'
                ),
                MessageAction(
                    label='12',
                    text='點/12'
                )
            ]
        
        ),
        CarouselColumn(
            title='13-15',
            text='13-15',
            actions=[
                MessageAction(
                    label='13',
                    text='點/13'
                ),
                MessageAction(
                    label='14',
                    text='點/14'
                ),
                MessageAction(
                    label='15',
                    text='點/15'
                )
            ]
        
        ),
        CarouselColumn(
            title='16-18',
            text='16-18',
            actions=[
                MessageAction(
                    label='16',
                    text='點/16'
                ),
                MessageAction(
                    label='17',
                    text='點/17'
                ),
                MessageAction(
                    label='18',
                    text='點/18'
                )
            ]
        
        ),
    ])
    return TemplateSendMessage(alt_text='Carousel alt text', template=carousel_template)



#def createRestaurantFlex(restaurant):
#    menu = getMenu(restaurant)
#    contentsFlex= []
#    food_info = ""
#    for food_no in range(length(menu)):
#        if food_no == 0 :
#        else:
#            food_info = '{ "type": "button", "action": { "type": "message", "label": "' + str(menu[food_no][0]) + '.' + str(menu[food_no][1]) + str(menu[food_no][2]) + '", "text": "點/' + str(menu[food_no][0]) +'" },' + ' "style": "secondary" } '
#            contentsFlex.append(food_info)
#    return print(contentsFlex)
##                    {
##                      "type": "button",
##                      "action": {
##                        "type": "message",
##                        "label": "1.珍珠奶茶",
##                        "text": "點/1"
##                      },
##                      "style": "secondary"
##                    },
        


#def helpwithFlex() :
#    return FlexSendMessage(
#        alt_text='test',
#        contents={
#            "type": "bubble",
#            "body": {
#              "type": "box",
#              "layout": "vertical",
#              "contents": [
#                {
#                  "type": "text",
#                  "text": "Brown Cafe",
#                  "weight": "bold",
#                  "size": "xl"
#                },
#                {
#                  "type": "box",
#                  "layout": "vertical",
#                  "margin": "lg",
#                  "spacing": "sm",
#                  "contents": [
#                    {
#                      "type": "box",
#                      "layout": "baseline",
#                      "spacing": "sm",
#                      "contents": [
#                        {
#                          "type": "text",
#                          "text": "Tel:",
#                          "color": "#aaaaaa",
#                          "size": "sm",
#                          "flex": 1
#                        },
#                        {
#                          "type": "text",
#                          "text": "Miraina Tower, 4-1-6 Shinjuku, Tokyo",
#                          "wrap": True,
#                          "color": "#666666",
#                          "size": "sm",
#                          "flex": 5
#                        }
#                      ]
#                    }
#                  ]
#                }
#              ]
#            },
#            "footer": {
#              "type": "box",
#              "layout": "vertical",
#              "spacing": "sm",
#              "contents": [
#                {
#                  "type": "box",
#                  "layout": "horizontal",
#                  "contents": [
#                    {
#                      "type": "button",
#                      "action": {
#                        "type": "message",
#                        "label": "取消",
#                        "text": "取消/"
#                      },
#                      "color": "#0055A4",
#                      "style": "secondary"
#                    },
#                    {
#                      "type": "button",
#                      "action": {
#                        "type": "message",
#                        "label": "統計",
#                        "text": "統計/"
#                      },
#                      "style": "secondary",
#                      "color": "#FFFFFF"
#                    },
#                    {
#                      "type": "button",
#                      "action": {
#                        "type": "message",
#                        "label": "清除",
#                        "text": "清除/"
#                      },
#                      "style": "secondary",
#                      "color": "#EF4135"
#                    }
#                  ]
#                },
#                {
#                  "type": "box",
#                  "layout": "vertical",
#                  "contents": [
#                    {
#                      "type": "button",
#                      "action": {
#                        "type": "message",
#                        "label": "1.珍珠奶茶",
#                        "text": "點/1"
#                      },
#                      "style": "secondary"
#                    },
#                    {
#                      "type": "button",
#                      "action": {
#                        "type": "message",
#                        "label": "2.綠茶",
#                        "text": "點/2"
#                      },
#                      "style": "secondary"
#                    },
#                    {
#                      "type": "button",
#                      "action": {
#                        "type": "datetimepicker",
#                        "label": "action",
#                        "data": "hello",
#                        "mode": "date"
#                      }
#                    },
#                    {
#                      "type": "box",
#                      "layout": "vertical",
#                      "contents": [
#                        {
#                          "type": "button",
#                          "action": {
#                            "type": "message",
#                            "label": "3.紅茶",
#                            "text": "點/3"
#                          }
#                        }
#                      ],
#                      "cornerRadius": "10px",
#                      "borderColor": "#000000",
#                      "borderWidth": "3px"
#                    }
#                  ],
#                  "action": {
#                    "type": "message",
#                    "label": "action",
#                    "text": "hello"
#                  },
#                  "spacing": "5px",
#                  "background": {
#                    "type": "linearGradient",
#                    "angle": "90deg",
#                    "startColor": "#0055A4",
#                    "endColor": "#EF4135",
#                    "centerColor": "#FFFFFF"
#                  },
#                  "cornerRadius": "5px",
#                  "paddingAll": "8px",
#                  "borderColor": "#000000"
#                }
#              ],
#              "flex": 0
#            }
#          }
#    )


def createMenuContent(restaurant):
    food_list = []
    menu = order_lib.getMenu(restaurant)
    menu = menu[1:]
    for food_info in menu:
#        sample_food = {
#            "type": "button",
#            "action": {
#                "type": "message",
#                "label": "",
#                "text": ""
#            },
#            "style" : "secondary"
#        }
        sample_food = {
            "type": "box",
            "layout": "vertical",
            "contents": [
            {
            "type": "button",
            "action": {
            "type": "message",
            "label": "",
            "text": ""
            },
            "style" : "secondary",
#            "color": "#624d4d"
            }
            ],
            "cornerRadius": "10px",
            "borderColor": "#81D8D0",
            "borderWidth": "2px",
            "height": "30px",
            "justifyContent": "center"
        }
        food_json_string = sample_food
        food_json_string["contents"][0]["action"]["label"] = str(food_info[0]) + '. ' + food_info[1] + ' ' + food_info[2]
        food_json_string["contents"][0]["action"]["text"] = '點/' + str(food_info[0])
        food_list.append(food_json_string)
    return food_list


def createWithFlex(restaurant):
    menu = order_lib.getMenu(restaurant)
    content_test ={
            "type": "bubble",
            "size": "kilo", #micro
            "body": {
              "type": "box",
              "layout": "vertical",
              "contents": [
                {
                  "type": "text",
                  "text": "食啥",
                  "weight": "bold",
                  "size": "xl"
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "margin": "lg",
                  "spacing": "sm",
                  "contents": [
                    {
                      "type": "box",
                      "layout": "baseline",
                      "spacing": "sm",
                      "contents": [
                        {
                          "type": "text",
                          "text": "Tel:",
                          "color": "#aaaaaa",
                          "size": "sm",
                          "flex": 1
                        },
                        {
                          "type": "text",
                          "text": "來研考科繳錢",
                          "wrap": True,
                          "color": "#666666",
                          "size": "sm",
                          "flex": 5
                        }
                      ]
                    }
                  ]
                }
              ]
            },
            "footer": {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
#                {
#                  "type": "box",
#                  "layout": "horizontal",
#                  "contents": [
#                    {
#                      "type": "button",
#                      "action": {
#                        "type": "message",
#                        "label": "清除✂",
#                        "text": "清除/"
#                      },
##                      "color": "#0055A4",
#                      "color": "#0F9D58",
##                      "color": "#8F60BF",
#                      "height": "sm",
#                      "style": "secondary"
#                    },
##                    {
##                      "type": "button",
##                      "action": {
##                        "type": "message",
##                        "label": "重新點單",
##                        "text": "取消/"
##                      },
##                      "style": "secondary",
##                      "height": "sm",
##                      "color": "#EF4135"
###                      "color": "#F4B400"
###                      "color": "#6E8C03"
##                    },
#                    {
#                      "type": "button",
#                      "action": {
#                        "type": "message",
#                        "label": "統計✎",
#                        "text": "統計/"
##                          "type": "postback",
##                          "label": "統計✎",
##                          "data": "統計/"
#                      },
#                      "style": "secondary",
#                      "margin": "50px",
#                      "height": "sm",
##                      "color": "#FFFFFF"
##                      "color": "#F0F1F2"
#                      "color": "#F4B400"
#                    }
#                  ]
#                },
                {
                  "type": "box",
                  "layout": "horizontal",
                  "contents": [
                    {
                      "type": "button",
                      "action": {
                        "type": "message",
                        "label": "取消訂餐",
                        "text": "取消/"
                      },
                      "style": "secondary",
                      "height": "sm",
                      "color": "#EF4135"
#                      "color": "#F4B400"
#                      "color": "#6E8C03"
                    }
                  ]
                },
                {
                  "type": "box",
                  "layout": "vertical",
                  "contents": ""
                  ,
                  "action": {
                    "type": "message",
                    "label": "action",
                    "text": "hello"
                  },
                  "spacing": "5px",
                  "background": {
                    "type": "linearGradient",
                    "angle": "90deg",
#                   "startColor": "#0055A4",
#                    "startColor": "#8F60BF",
                    "startColor": "#0F9D58",
#                   "endColor": "#EF4135",
#                    "endColor": "#83A603",
                    "endColor": "#F4B400",
                    "centerColor": "#F0F1F2"
                  },
                  "cornerRadius": "5px",
                  "paddingAll": "8px",
                  "borderColor": "#000000"
                }
              ],
              "flex": 0
            }
          }
    content_test["footer"]["contents"][1]["contents"] = createMenuContent(restaurant)
    content_test["body"]["contents"][0]["text"] = str(menu[0][0])
    content_test["body"]["contents"][1]["contents"][0]["contents"][1]["text"] = str(menu[0][1]) + " 來文書科繳錢"
    #content_test["footer"]["contents"][1] = { "type" : "text", "text" : "hello" }
    return FlexSendMessage(
        alt_text='Carte de Menu',
        contents= content_test
    )

