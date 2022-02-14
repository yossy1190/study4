課題４ー６

【課題目標】
お客様からのお預かり金額を入力しお釣りを計算する

【行ったこと】
・Orderclass内に、pay_total_moneyメソッドを追加。
→inputで預入金額を入力させる。pay_moneyに格納。
→add_order_listメソッドで計算したalltotalからpay_moneyを差し引き、change_moneyに格納。
→printで、change_moneyを含めて、メッセージを出力

・pay_total_moneyをmain関数で実行

【作業の際に困ったこと】
・メソッドを定義する際に、どのタイミングでselfを使うのか、インスタンスの引数とするのか、
　少し混乱してしまったた。
 →再度復習。Class内で定義している変数を呼び出すときは、selfをつける？
