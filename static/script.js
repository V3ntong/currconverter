// Example of a quick UI interaction
const input = document.querySelector('input[name="amount"]');
input.addEventListener('input', (e) => {
    if(e.target.value < 0) {
        alert("Please enter a positive number");
        e.target.value = "";
    }
});