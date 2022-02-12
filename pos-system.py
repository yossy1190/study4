
import csv

### 商品クラス
class Item:

    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
        # self.num=num


    def getitem_code(self):
        return self.item_code

### オーダークラス
class Order:
    # コンストラクタ　
    def __init__(self,item_masters):
        self.item_order_list=[]
        self.item_masters=item_masters

    
    def print_order_item(self,item_code):
        # インスタンスのitem_mastersから、１つずつ値を取り出し、引数の商品コードと符合する商品を探す。
        # その商品の、ID・名前・価格をprintメソッドで表示させる。
        for master in self.item_masters:
            if item_code==master.item_code:
                print(f"商品コード:{master.item_code},商品名:{master.item_name},価格:{master.price}")

                
    def add_order_list(self):
        # item_order_listにinputの内容を格納していく。
        while True:
            val=input("商品コードを入力(001～999)。Enterのみで精算します。:")         
            if val:
                self.item_order_list.append(val)           
            else:
                break
        for item in self.item_order_list:
            self.print_order_item(item)
        # return order_list
    
### メイン処理　関数main
def main():
    
    # マスター登録。二次元配列用の箱を準備
    items_in=[]
    
    # csvファイルのデータを読み取る。変数listsとして呼び出し可能にしておく。
    # headerが邪魔なので、２行目から読み取る
    # 変数listsから値を取り出し変数itemに格納。二次元配列items_inにリストとしてappendしていく。
    # for文で、インスタンス化を繰り返し処理する。
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
    

    
if __name__ == "__main__":
    main()
