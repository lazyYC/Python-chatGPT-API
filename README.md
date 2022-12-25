# Unofficial-chatGPT-API
A python chatGPT API module made by LazyYC
# 
# 
### As its name, this is a handy chatGPT API (unofficial) since OpenAI has not been released their one yet.
# 
## 如何使用 <br/>How to use?
# 
### 1. 獲得你的權限token  <br/> get your auth token
### 
#### 1-1 到OpenAI的網站 <br> go to https://chat.openai.com/chat  

#### 
#### 1-2 按F12找到應用程式裡面的cookies <br/> press F12 and find "cookies" at application

#### 
#### 1-3 選"__Secure-next-auth.session-token"並複製後面一長串的值 <br/> check "__Secure-next-auth.session-token" and copy the value

#### 
![image](https://user-images.githubusercontent.com/71726501/209456014-0076c303-6a4f-460b-84a6-a3aacb48f24b.png)


### 2. API
#### 
```
from chatgpt_api import chatgpt_api
api = chatgpt_api(
    # your token
)
api.open_browser()
```

<br/>

```
# 傳入訊息
# send message to chatGPT
resp = api.send_message('good morning')
print(resp)
```
#### Response
<img width="300" alt="image" src="https://user-images.githubusercontent.com/71726501/209455949-78240372-ce8e-40e7-b961-88523f30903d.png">


#### 你也可以指定輸出語言，目前只提供繁簡中文和英文 <br/> you can also specify a language you want chaTGPT replay with, now only English, ZH-TW and ZH-CN are supported. 
```
resp = api.send_message('What can I do if I lose my sleep?', 'zhtw')
print(resp)
```
<img width="473" alt="image" src="https://user-images.githubusercontent.com/71726501/209456147-fc27662e-9939-4222-8ab4-ba10c8184195.png">
<br/>
<br/>
### 功能陸續增加中，邊做邊學邊練習

