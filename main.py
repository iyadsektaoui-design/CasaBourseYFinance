from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API بورصة الدار البيضاء تعمل بنجاح!"}

@app.get("/stock/{ticker}")
def get_stock(ticker: str):
    # إضافة .MA تلقائياً إذا نسيها المستخدم
    symbol = f"{ticker}.MA" if ".MA" not in ticker.upper() else ticker
    
    stock = yf.Ticker(symbol)
    hist = stock.history(period="5d") # جلب آخر 5 أيام
    
    if hist.empty:
        return {"error": "لم يتم العثور على بيانات لهذا الرمز"}
    
    return {
        "symbol": symbol,
        "current_price": hist['Close'].iloc[-1],
        "history": hist['Close'].to_dict()
    }