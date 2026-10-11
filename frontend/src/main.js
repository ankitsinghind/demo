const mybutton = document.getElementById("testbtn");
const mytest = document.getElementById("result");

mybutton.addEventListener("click", async function () {
  const response = await fetch("http://localhost:8000/api/test");
  const data = await response.json();
  mytest.textContent = data.message;
});
