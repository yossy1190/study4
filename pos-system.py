### 商品クラス
from re import I

class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price

    def GetItem_code(self):
        return self.item_code

### オーダークラス
class Order:
    # コンストラクタ　
    def __init__(self,item_masters):
        self.item_order_list=[]
        self.item_masters=item_masters
        
    def Order_Item_Info(self,item_code):
        # インスタンスのitem_mastersから、１つずつ値を取り出し、引数の商品コードと符合する商品を探す。
        # その商品の、ID・名前・価格をprintメソッドで表示させる。
        for master in self.item_masters:
            if item_code==master.item_code:
                print("商品コード:{},商品名:{},価格:{}".format(master.item_code,master.item_name,master.price))


### メイン処理　関数main
def main():

    # この店の商品(item)一覧情報をここで取り込み。
    # ここではまだorderクラスはインスタンス化してない。
    item_masters=[]
    item_masters.append(Item("001","りんご",100))
    item_masters.append(Item("002","なし",120))
    item_masters.append(Item("003","みかん",150))

    # orderクラスをインスタンス化。Order_Item_Infoメソッドを使えるようにする。
    # 商品コードを引数入力したら、ID・名前・価格をprintメソッドで表示させる。
    order=Order(item_masters)
    order.Order_Item_Info("001")
    order.Order_Item_Info("002")
    order.Order_Item_Info("003")
    
if __name__ == "__main__":
    main()
