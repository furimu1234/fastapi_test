from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#APIを作るうえで必要なツールをインポート

#高速に処理を行うためのツールをインポート
import numpy as np


# 変数名: クラス名 = クラス名("パラメーター群")

#変数名: クラス名 と書くことにより、エディター等でメソッドやプロパティが表示されやすくなる

#FastAPIをインスタンス化
app: FastAPI = FastAPI()

#templateの設定
template: Jinja2Templates = Jinja2Templates("template")

#CSSのファイルパスを設定
app.mount("/static", StaticFiles(directory="static"), name="static")


#http:xxx.xxx.xxx/　にアクセスされた時に index.html の中身を表示する。
@app.get("/", response_class=HTMLResponse)
async def test(req: Request):
    
    #test1, test2の値をそれぞれ、 index.htmlで使えるようにする。
    data = {"request": req,"test1": "test1", "test2": "test2"}
    
    return template.TemplateResponse("index.html", data)


@app.get("/random", response_class=HTMLResponse)
async def random(req: Request):
    #配列の生成
    li = ["ビジネス", "CG・CAD", "システム"]

    #配列からどれかをとりだして、 rd 変数に代入する
    rd = np.random.choice(li)
    
    #rd変数の中身を random.html で使えるようにする
    data = {"request": req,"random_data": rd}

    return template.TemplateResponse("random.html", data)