#from linebot import (
#    LineBotApi, WebhookHandler)

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
#    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
#    TextComponent, IconComponent, ButtonComponent,
#    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage)


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
