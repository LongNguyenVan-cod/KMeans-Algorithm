# KMeans-Algorithm
Sử dụng thuật toán KMeans bằng thư viện Scikit-learn để xử lý hình ảnh, giảm kích thước file ảnh, khâu chuẩn bị cho máy học.
## Chuẩn hóa hình ảnh
Trước khi có thể áp dụng thuật toán cần chuẩn hóa lại định dạng của ảnh cần xử lý <br \>
Ban đẩu ảnh được thể hiện dưới dạng matrix với b hàng và a cột, <br \>
mỗi phần tử trong matrix tương đương với một điểm ảnh (pixel) với giá trị tương đương giá trị màu của điểm ảnh trong ảnh. <br \>
![Screenshot_20250604_202414_com huawei hinote](https://github.com/user-attachments/assets/9d88297c-d9e0-4227-bcbe-9f800ecfb968)
Từ dạng matrix ảnh sẽ được đưa về dạng mảng 1 chiều bằng cách duỗi các điểm ảnh trong cùng một hàng thành cùng một cột <br \>
và làm lần lượt từng hàng trong matrix của ảnh. <br \>
![Screenshot_20250604_202522_com huawei hinote](https://github.com/user-attachments/assets/e1a58d10-6e16-433d-beaa-d49f4e582e67)
## Chọn số cụm - k
Việc chọn số cụm phù hợp thì việc xử lý ảnh mới có hiệu quả. <br \>
Có nhiều phương pháp để chọn được số cụm phù hợp, tôi sử dụng Elbow Method để chọn k từ việc tính toán khoảng cách <br \>
Euclidean giữa các điểm ảnh ban đầu với điểm ảnh tương ứng sau phân cụm. <br \>
![Figure_k](https://github.com/user-attachments/assets/9ed72da2-0daf-4f53-9825-2db4e2953ea5)
