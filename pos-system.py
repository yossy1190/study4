
import csv
import datetime
from pathlib import Path

### 商品クラス
class Item:

    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price

    def getitem_code(self):
        return self.item_code

### オーダークラス
class Order:
    # item_mastersの中には、CSVで読み込んだ、code,name,priceが入る
    def __init__(self,item_masters):
        self.item_order_list=[]
        self.item_amount_list=[]
        self.item_masters=item_masters
        self.subtotal=0
        self.alltotal=0
        self.pay_money=0
        self.change_money=0
        self.pay_money=0
        self.change_money=0

    def add_order_list(self):
        # item_order_listにinputの内容を格納していく。
        while True:
            val=input("商品コード(001～999)を入力してください。注文終了時はEnterキーのみで精算します。>>>") 
            if val:
                self.item_order_list.append(val)
                amt=input("商品個数はいくつですか？>>>")        
                self.item_amount_list.append(amt)           
            else:
                break     
        # 入力された、商品コードと商品個数を１つずつ取り出す。print_order_item関数に当てる
        
        for val_item_code,amount in zip(self.item_order_list,self.item_amount_list):
            self.print_order_item(val_item_code,amount)
            self.alltotal=self.alltotal+self.subtotal
            self.subtotal=0
        print(f"会計金額:{int(self.alltotal):,}円")
        
            
            
    def print_order_item(self,val_item_code,amount):
            # item_mastersから１つのitemを取り出し、item_code,item_name,priceにアクセスできるようにする。
            # 入力されたitem_codeがitem_mastersに含まれているか確認。
            
            for item in self.item_masters:
                
                if val_item_code in item.item_code:
                    
                    self.subtotal = int(item.price)*int(amount)
                    print(f"商品コード:{item.item_code},商品名:{item.item_name},価格:{int(item.price):,}円,個数{amount}個")
            print(f"小計:{int(self.subtotal):,}円")
            
        
    def pay_total_money(self):
        
        self.pay_money=int(input(f"お会計は{int(self.alltotal):,}円です。預け入れ金額を入力してください(円不要)。>>>"))
        self.change_money=self.pay_money-int(self.alltotal)
        print(f"お支払いありがとうございます。お釣りは{self.change_money:,}円です。本日はご来店ありがとうございました!")
       
    
    def print_receipt(self):
        payment_date=datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        
        with open("receipt.txt","w",encoding="utf-8") as f:
            f.write(f"来店日時:{payment_date}\n")
            l=len(self.item_order_list)
            for i in range(l):
                f.write(f"商品コード:{self.item_order_list[i]},商品名:{self.item_masters[i].item_name},価格:{self.item_masters[i].price}円,個数{self.item_amount_list[i]}個\n")
            f.write(f"合計金額:{int(self.alltotal):,}円\nお預かり金額:{int(self.pay_money):,}円\n")
            f.write(f"お釣り:{int(self.change_money):,}円\n")
            f.write("本日はご来店ありがとうございました！")
    
### メイン処理　関数main
def main():
    
    # マスター登録。二次元配列用の箱を準備
    items_in=[]
    
    with open("item.csv","r",encoding="Shift-JIS") as lists:
        header=next(csv.reader(lists))
        for list in csv.reader(lists):
            items_in.append(list)
            
    item_masters=[]    
    for item_in in items_in:
        item_masters.append(Item(*item_in))

    # orderクラスをインスタンス化。Order_Item_Infoメソッドを使えるようにする。
    # order_listへの追加は、Orderクラスにメソッドとして記入。mainでは、メソッド呼び出しのみにする。
    order=Order(item_masters)
    order.add_order_list()
    order.pay_total_money()
    order.print_receipt()
    
if __name__ == "__main__":
    main()
