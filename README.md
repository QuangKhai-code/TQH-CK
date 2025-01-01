# Dashboard Phân Tích Nhà Thuốc & Cơ Sở Khám Bệnh tại TP. Hồ Chí Minh

## Tổng Quan

Dự án này cung cấp bảng điều khiển tương tác (dashboard) và chatbot hỗ trợ truy vấn thông tin, giúp người dùng dễ dàng khám phá và phân tích dữ liệu về nhà thuốc và cơ sở khám bệnh tại TP. Hồ Chí Minh. Bằng cách sử dụng **Tableau** để tạo các bảng điều khiển và **Streamlit** để xây dựng chatbot, chúng tôi mang đến giải pháp toàn diện để trực quan hóa và tương tác với dữ liệu.

## Tính Năng

- **Hiển thị dữ liệu trực quan**:
  - Sử dụng Tableau để tạo biểu đồ và bản đồ phân tích số lượng nhà thuốc, cơ sở khám bệnh.
  - Trực quan hóa phân bổ theo quận/huyện, so sánh các khu vực nội thành và ngoại thành.
- **Chatbot hỗ trợ truy vấn**:
  - Xây dựng trên Streamlit, chatbot giúp trả lời câu hỏi liên quan đến dữ liệu, như:
    - "Quận nào có số lượng nhà thuốc nhiều nhất?"
    - "Số lượng cơ sở khám bệnh ở Quận 10 là bao nhiêu?"
- **Phân tích nâng cao**:
  - Gợi ý các khu vực cần đầu tư thêm dựa trên mật độ dân số và nhu cầu chăm sóc sức khỏe.
- **Trích xuất báo cáo**:
  - Hỗ trợ tải xuống các báo cáo dưới dạng hình ảnh hoặc file PDF.

## Công Nghệ Sử Dụng

### Phân Tích Dữ Liệu
- **Tableau**:
  - Tạo bảng điều khiển tương tác và biểu đồ trực quan.

### Xây Dựng Chatbot
- **Streamlit**:
  - Framework để xây dựng ứng dụng chatbot tương tác.
  - Kết nối với Tableau để truy vấn và hiển thị dữ liệu từ dashboard.
- **OpenAI API hoặc các NLP Framework**:
  - Tích hợp xử lý ngôn ngữ tự nhiên, giúp chatbot hiểu và trả lời các câu hỏi.

### Triển Khai
- **Frontend**:
  - Giao diện người dùng được triển khai qua Streamlit.

