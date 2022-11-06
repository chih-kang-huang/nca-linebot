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


def helpWithCarousel():
    """ Return help message text with carousel template 
    If there is an image, there have to be images at every cols
    """
    carousel_template = CarouselTemplate(columns=[
        CarouselColumn(thumbnail_image_url='https://imgur.com/gallery/p2DNWk3',
                       title='訂', 
                       text='試試看這個範例！', 
                       actions=[
                           MessageAction(label='範例', 
                           text='指令輸入格式：[指令]/[內容1]/[內容2]...\n\
                                 指令：說明、吃、點、取消、統計、截止、清除')
        ]),
        CarouselColumn(thumbnail_image_url='https://imgur.com/gallery/p2DNWk3',
                       title='來源', 
                       text='請查看：', 
                       actions=[
                           URIAction(label='GitHub Repo', uri='https://github.com/CheesyPicodon/ncu-line-bot')
        ])
        
    ])
    return TemplateSendMessage(alt_text='Carousel alt text', template=carousel_template)
