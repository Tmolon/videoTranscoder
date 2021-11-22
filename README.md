# videoTranscoder
FFmpeg+ Celery+ redis+ Django toplamından oluşan bir video converter çalışması

Bu çalışmada video process gerçekleştirmek için farklı teknolojileri bir arada kullanmaya çalıştım. Video dönüştürme işlemini,
bir web uygulamasında doğrudan onclick ile tetiklerseniz kullanıcı işlemde geçen süre boyunca beklemek zorunda kalacaktır. Bu bizim istemediğimiz bir durumdur.
Bu durumu aşmak için proccessleri arka planda worker olarak çalıştırma fikri cazip geliyor. 

İşte bu noktada celery kütüphanesi ciddi işler çıkartıyor. Bu projede celery kullanarak video process işlemlerini gerçekleştiriyoruz. Tabi ki celery'e atadığımız
processler FFmpeg sayesinde iş yapıyor. FFmpeg de nedir diyenler için kabaca video manipülsayon işlemlerini bize sağlayan bir open source kütüphane diyebiliriz.
Workerlar ise redis sayesinde sırayla iş alıyor ve görevlerini tamamlıyorlar. Tüm bu server side işlemleri tabiki de django üzerinde gerçekleştiriyoruz.
