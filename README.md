# ChatPDF
ChatPDF là một ứng dụng web cho phép người dùng tải lên PDF và trò chuyện với nội dung của họ bằng các mô hình AI như Gemini và Deepseek. Được xây dựng với Reactjs, TypeScript và TailWindCSS, nó có giao diện người dùng thân thiện với người dùng với Google OAuth2 và tóm tắt. Phần phụ trợ Django với Redis và AI API đảm bảo tương tác tài liệu hiệu quả, an toàn cho sinh viên và chuyên gia

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
![Image](https://github.com/user-attachments/assets/7ee9c705-97c8-45db-9424-229158a63e9f)
![Image](https://github.com/user-attachments/assets/e9a4218b-4cc1-4a08-b4a8-166b18290a6b)
![Image](https://github.com/user-attachments/assets/17eb232f-5a47-42d8-a5f4-76616b35e948)
![Image](https://github.com/user-attachments/assets/749372a9-73a0-49d2-b1dd-6ffc1e2082ec)
![Image](https://github.com/user-attachments/assets/28a42cec-41cf-48c5-a620-e29393b34ba5)
![Image](https://github.com/user-attachments/assets/eb6d6b99-f9fc-411b-8240-36ea2ea530c9)
![Image](https://github.com/user-attachments/assets/f7bd624e-cf21-43f3-80b0-20054208ee29)
![Image](https://github.com/user-attachments/assets/9a32a3bf-c106-4084-90e9-e4ba8de3de98)
![Image](https://github.com/user-attachments/assets/7df89efe-b4e3-49de-b15e-ef9b771bc6cd)

Conversation
![Image](https://github.com/user-attachments/assets/b80d3e48-9964-4e61-b285-b91541eecd66)

Select model AI <br>
![Image](https://github.com/user-attachments/assets/4b9f673d-1d2a-4032-bf39-0a490c823025)

Upload file
![Image](https://github.com/user-attachments/assets/8525dd9c-cb86-49c8-a7c9-5051a48ef02e)

![Image](https://github.com/user-attachments/assets/a2bb5649-4c51-416a-97e1-10c25f30fb2d)

![Image](https://github.com/user-attachments/assets/47a172bb-2096-4591-a286-770211c3b7bc)

Edit name:
![Image](https://github.com/user-attachments/assets/81d39d21-52a4-4b16-821c-ecb3d9b5cd7d)

![Image](https://github.com/user-attachments/assets/a87f2f74-75a2-47fc-8247-ca88ebd98ac8)

![image](https://github.com/user-attachments/assets/6fe25ec8-e634-40e4-81bc-8391ef50f434)


Delete conversation:
![image](https://github.com/user-attachments/assets/0c95486f-4212-43a0-87d5-6fc037a48939)


![Image](https://github.com/user-attachments/assets/d1fdd231-2437-4727-9c27-e1b1e3b1abc1)

Summary conversation <br>
![Image](https://github.com/user-attachments/assets/d9fb9956-2d27-4c0b-8a62-cb0b71f6d98c)

![Image](https://github.com/user-attachments/assets/03762e63-59c2-4b56-9e68-fa0e3ee1d750)

![Image](https://github.com/user-attachments/assets/a9b798f8-2d9b-40d9-b77e-3d2ccf1c7e0e)
