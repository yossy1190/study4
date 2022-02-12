
import csv

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


### メイン処理　関数main
def main():
   

    # 二次元配列用の箱を準備
    items_in=[]
   
    # 商品マスタをcsvで読み込みできるようにする！
    #csvファイルのデータを読み取る。変数listsとして呼び出し可能にしておく。
    # headerが邪魔なので、２行目から読み取る
    with open("item.csv","r",encoding="Shift-JIS") as lists:
        header=next(csv.reader(lists))
        
    # 変数listsから値を取り出し変数itemに格納。二次元配列items_inの中にappendしていく。
        for item in csv.reader(lists):
            items_in.append(item)

    # for文で、インスタンス化を繰り返し処理する。item_mastersはItemクラスを要素に持つ配列。
    item_masters=[]    
    for item_in in items_in:
        item_masters.append(Item(*item_in))



    # orderクラスをインスタンス化。Order_Item_Infoメソッドを使えるようにする。
    # 商品コードを引数入力したら、ID・名前・価格をprintメソッドで表示させる。
    order=Order(item_masters)
    
    #買い物かご(order_lists)を作成
    #inputによりコンソール画面で、商品コードを入力させる。
    # while文を使って、注文したものをappendし続ける。
    order_lists=[]
    while True:
        val=input("商品コードを入力(001～999)。Enterのみで精算します。:")
        if val:
            order_lists.append(val)
        else:
            break
    
    #order_listsをfor文で回して、inputで入力させた商品コードを変数itemに代入。
    #変数itemを、print_order_itemメソッドに当てる。
    for item in order_lists:
        order.print_order_item(item)
    
if __name__ == "__main__":
    main()
