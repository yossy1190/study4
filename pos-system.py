### 商品クラス
from re import I


class Item:

    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price

    
    def GetItem_code(self):
        return self.item_code
    
    def GetItem_name(self):
        return self.item_name
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    # コンストラクタ　
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code,item_name,price):
        # item_order_listにitem_name,priceを格納するために追記
        self.item_order_list.append(item_code)
        self.item_order_list.append(item_name)
        self.item_order_list.append(price)
    
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))

### メイン処理　関数main
def main():

    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))

    # 注文したcode、name,priceをaddしていく。item_order_listにaddされる。
    order=Order(item_master)
    order.add_item_order("001","りんご",100)
    order.add_item_order("002","なし",120)
    order.add_item_order("003","みかん",150)
   
    order.view_item_list()
    
if __name__ == "__main__":
    main()