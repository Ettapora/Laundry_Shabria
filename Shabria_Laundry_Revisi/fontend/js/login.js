document.getElementById('loginForm').addEventListener('submit', function(e) {
    // Biar halamannya nggak nge-refresh otomatis pas diklik Masuk
    e.preventDefault(); 
    
    // Ambil nilai dari inputan
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // SIMULASI LOGIN (Karena backend lagi rehat)
    if (email === 'bryan@shabrialaundry.com' && password === 'admin123') {
        alert('Berhasil masuk bosku! (Mode Simulasi Frontend)');
        
        // Kalau lu udah bikin file dashboard.html, buka komen di bawah ini:
        // window.location.href = 'dashboard.html';
    } else {
        alert('Email atau password salah! Cek lagi akun demonya.');
    }
});