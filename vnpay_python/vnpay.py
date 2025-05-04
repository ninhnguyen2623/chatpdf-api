import hashlib
import hmac
import urllib.parse

class vnpay:
    requestData = {}
    responseData = {}

    def get_payment_url(self, vnpay_payment_url, secret_key):
        inputData = sorted(self.requestData.items())
        queryString = ''
        for key, val in inputData:
            if len(queryString) > 0:
                queryString = queryString + "&" + key + "=" + urllib.parse.quote_plus(str(val))
            else:
                queryString = key + "=" + urllib.parse.quote_plus(str(val))

        hashValue = self.__hmacsha512(secret_key, queryString)
        print("Payment HashData:", queryString)
        print("Payment HashValue:", hashValue)
        return vnpay_payment_url + "?" + queryString + '&vnp_SecureHash=' + hashValue

    def validate_response(self, secret_key):
        # Log chi tiết dữ liệu phản hồi
        print("Response data:", self.responseData)
        
        # Kiểm tra chữ ký
        if 'vnp_SecureHash' not in self.responseData:
            print("No vnp_SecureHash found")
            return False
        
        # Lấy chữ ký từ phản hồi
        vnp_secure_hash = self.responseData['vnp_SecureHash']
        
        # Tạo bản sao của dữ liệu phản hồi và loại bỏ các trường hash
        data = self.responseData.copy()
        if 'vnp_SecureHash' in data:
            data.pop('vnp_SecureHash')
        if 'vnp_SecureHashType' in data:
            data.pop('vnp_SecureHashType')
        
        # QUAN TRỌNG: Chuyển đổi từ kiểu QueryDict sang dict
        # Trong callback, đôi khi Django cung cấp dữ liệu ở định dạng đặc biệt
        if hasattr(data, 'dict'):
            data = data.dict()
        
        # Sắp xếp theo thứ tự từ điển
        sorted_data = sorted(data.items())
        
        # Xây dựng chuỗi để tạo hash - thử nhiều cách khác nhau
        hash_data = ""
        for key, val in sorted_data:
            if len(hash_data) > 0:
                hash_data += "&" + key + "=" + str(val)
            else:
                hash_data = key + "=" + str(val)

        # THỬ NGHIỆM: VNPay có thể không mã hóa URL trong callback
        # Nếu cách trên không hoạt động, hãy thử cách này
        plain_hash_data = hash_data
        
        # Tính toán hash từ chuỗi
        calculated_hash = self.__hmacsha512(secret_key, plain_hash_data)
        
        # In ra để kiểm tra
        print("Plain hash data:", plain_hash_data)
        print("Calculated hash:", calculated_hash)
        print("Received hash:", vnp_secure_hash)
        
        # So sánh hash
        result = vnp_secure_hash.lower() == calculated_hash.lower()
        print("Hash validation result:", result)
        
        return result

    @staticmethod
    def __hmacsha512(key, data):
        # Key và data phải là bytes
        byteKey = key.encode('utf-8')
        byteData = data.encode('utf-8')
        return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()