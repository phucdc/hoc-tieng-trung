const p = document.getElementById("message");
let i = 5;

function countdown() {
  if (i > 0) {
    const message = "You will be redirected to home page in " + i + " seconds";
    p.innerHTML = message;
    i--;
    setTimeout(countdown, 1000);
  } else {
    window.location.href = "/";
  }
}

countdown();
