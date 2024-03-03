css = '''
<style>
.css-18ni7ap[data-testid="stHeader"]{
    background-image: url("isaksham.png");
    background-size: cover;
}
#inspection-co-pilot {
    padding-top: 0;
}
.blcok-container {
    padding-top: 0;
}
.st-emotion-cache-10trblm {
    position: relative;
    flex: 1 1 0%;
    margin-left: calc(3rem);
    color: rgb(215,130,28);
}
.element-container div[data-test-id="stImage"]{
    position: absolute
    top: 32px;
    left: -32%
}
.css-h5rgaw a {
    color: rbb(255 255 255 / 0%);
}
.css-h5rgaw {
    color: rbb(255 255 255 / 0%);
}

.chat-message{
    border-radius: 0.5rem;
    padding: 16px;
    display: flex;
    margin-top: 20px;
    margin-bottom: 30px;
}
.chat-message.user{
    background-color: #ffffffe0;
    float: left;
    border-radius: 0px 26px 26px 26px;
    width: 90%;
    color: #333;
}
.st-b7 {
    background-color: #fff!important
}
.chat-message.bot{
    background-color: #441f54db;
    float: right;
    border-radius: 16px 0px 16px 16px;
    width: auto;
    padding: 14px;
    color: #fff;
}

.chat-message.user::after,
.chat-message.bot::before{
    position: absolute;
    top: -40px;
    background-repeat: no-repeat;
    background-size: contain
    color: #666;
}
.chat-message.user::after{
    background-size: 40px;
    pdding-left: 42px;
    display: flex;
    background-position-y: center;
    left: 0;
    content: "Sales Analytics CoPilot";
    font-weight: 600;
}
.chat-message.bot::before{
    content: "You";
    right: 0;
    background-image: url('https://cdn-icons-png.flaticon.com/512/149/149071.png');
    background-size: 20px;
    padding-right: 24px;
    background-position: right;
    filter: grayscale(0.3);
    font-weight: 600;
}
.chat-message .avatar {
    width: 12%;
}
.chat-message .avatar img{
    max-width: 60px;
    max-height: 40px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: auto;
    padding: 0 .35rem;
}

div[data-baseweb="input"]{
    height: 52px;
    border: 1px solid #62656b;
    border-radius: 16px;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="messsage">{{MSG}}</div>
</div>
'''
user_template = '''
<div class="chat-message user">
    <div class="messsage">{{MSG}}</div>
</div>
'''
