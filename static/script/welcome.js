//Instagram
let insta = document.getElementById("insta")

insta.addEventListener("mouseenter", function() {
    insta.src = '../static/img/instagram.png'
});

insta.addEventListener("mouseleave", function() {
    insta.src = '../static/img/instagramblack.png'
});

//Linkedin
let linkedin = document.getElementById("linkedin")

linkedin.addEventListener("mouseenter", function() {
    linkedin.src = '../static/img/linkedin.png'
});

linkedin.addEventListener("mouseleave", function() {
    linkedin.src = '../static/img/linkedinblack.png'
});

//Youtube
let youtube = document.getElementById("youtube")

youtube.addEventListener("mouseenter", function() {
    youtube.src = '../static/img/youtube.png'
});

youtube.addEventListener("mouseleave", function() {
    youtube.src = '../static/img/youtubeblack.png'
});

//Spotify
let spotify = document.getElementById("spotify")

spotify.addEventListener("mouseenter", function() {
    spotify.src = '../static/img/spotify.png'
});

spotify.addEventListener("mouseleave", function() {
    spotify.src = '../static/img/spotifyblack.png'
});

const botao = document.getElementById("copiar")
const areacopiar = document.getElementById("areacopiar")

function copiarSenha(){
    let senha = document.getElementById("senha").innerText;
    navigator.clipboard.writeText(senha)
    botao.innerText = "Senha Copiada"
    
    setTimeout(() => {
        botao.innerText = "Copiar a Senha"
    }, 1500);
    
}

areacopiar.addEventListener("click", copiarSenha)