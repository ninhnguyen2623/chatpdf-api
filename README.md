# ChatPDF
ChatPDF là một ứng dụng web cho phép người dùng tải lên PDF và trò chuyện với nội dung của họ bằng các mô hình AI như Song Tử và Deepseek. Được xây dựng với Reactjs, TypeScript và TailWindCSS, nó có giao diện người dùng thân thiện với người dùng với Google OAuth2 và tóm tắt. Phần phụ trợ Django với Redis và AI API đảm bảo tương tác tài liệu hiệu quả, an toàn cho sinh viên và chuyên gia

## Công nghệ được sử dụng:
-Frontend: TypeScript, ReactJS, Redux Toolkit (Quản lý trạng thái), Axios (Yêu cầu API), TailWindcss, ANT Design, React-PDF-Viewer (kết xuất PDF), VITE (công cụ xây dựng). <br>
-Backend: Python 3.x, Django (API RESTful), Django Rest Framework, SimpleJWT (Xác thực JWT), Django-Allauth (Google OAuth2), Redis (bộ nhớ đệm), PYPDF2 (xử lý PDF)
## AI API: Google Gemini, OpenRouter (Deepseek, Llama, Qwen)

## Các tính năng chính
- Thiết kế giao diện xác thực an toàn với đăng nhập/đăng ký, tích hợp Google OAuth2 và xử lý mã thông báo JWT làm mới chắc chắn, và chức năng quên mật khẩu với mật khẩu mưới gưi qua email sử dụng Redux để quản lý trạng thái người dùng và Axios để tương tác API. <br>

- Xây dựng tính năng quản lý tải lên PDF và thực hiện lưu trữ trên server, kết hợp Reac-pdf-viewer để hiển thị với từng cuộc hội thoại trong trình duyệt và giao diện trò chuyện. Đồng thời trích xuất nội dung PDF tự động bằng PyPDF2 để cung cấp dữ liệu cho AI. <br>

- Tích hợp nhiều mô hình AI ngôn ngữ tự nhiên (Gemini, DeepSeek, Llama, Qwen) thông qua API từ Google, OpenRouter. Cho phép người dùng chọn mô hình AI thông qua giao diện ModeSelect để trò chuyện. Sử dụng Redis để lưu ngữ cảnh PDF giữa các tin nhắn trong cùng cuộc hội thoại, tối ưu hóa hiệu suất. <br>

- thực hiện tóm tắt hội thoại và xuất báo cáo nội dung hoặc nêu các ý chính của cuộc hội thoại bằng AI, hiển thị dưới dạng tin nhắn và file Word tải xuống <br>

- Quản lý lịch sử hội thoại hiển thị danh sách các cuộc hội thoại với tiêu đề và PDF liên kết. Hỗ trợ xóa hội thoại (bao gồm xóa ngữ cảnh trong Redis) và chỉnh sửa tiêu đề đồng thời lưu trữ tin nhắn và tóm tắt vào cơ sở dữ liệu thông qua API. <br>


Register:
![Image](https://github.com/user-attachments/assets/70a7b029-c28a-476c-9a3e-a295a782222f)

Login:
![Image](https://github.com/user-attachments/assets/6a2fc5ba-473f-45e1-8207-2234baac6b76)

Home:
![Image](https://github.com/user-attachments/assets/66b42fe7-5975-4c21-ade3-5fcbe8c27bdf)

Conversation
![Image](https://github.com/user-attachments/assets/02e03d2f-c3eb-4aa8-b196-d177948bd7fb)

Select model AI <br>
![Image](https://github.com/user-attachments/assets/4b9f673d-1d2a-4032-bf39-0a490c823025)

Upload file
![Image](https://github.com/user-attachments/assets/81d2b3f3-7635-4d09-8c9d-ef30fa851ccd)

![Image](https://github.com/user-attachments/assets/b3bf3cf2-258a-4827-b6b4-f42fb7d848e9)

![Image](https://github.com/user-attachments/assets/116f00ca-e6e3-4984-abac-28e1a2f38695)

Edit name:
![Image](https://github.com/user-attachments/assets/38de6db5-a50e-4b2e-9d25-16d201a15cbe)

![Image](https://github.com/user-attachments/assets/342ba3d3-d34e-4699-b34e-d410a9d4f03a)

![Image](https://github.com/user-attachments/assets/507a3c2e-f87b-4816-8a9f-d6624f621840)

Delete conversation:
![Image](https://github.com/user-attachments/assets/a31964b2-85fb-495b-8412-27622c4fbbbf)

![Image](https://github.com/user-attachments/assets/344bae75-55e9-4799-90cc-7b4930f86ed9)

Summary conversation
![Image](https://github.com/user-attachments/assets/d9fb9956-2d27-4c0b-8a62-cb0b71f6d98c)

![Image](https://github.com/user-attachments/assets/03762e63-59c2-4b56-9e68-fa0e3ee1d750)

![Image](https://github.com/user-attachments/assets/a9b798f8-2d9b-40d9-b77e-3d2ccf1c7e0e)
