const toggleButton = document.querySelector(".toggle_btn")
const dropDownMenu = document.querySelector(".dropdown_menu")

toggleButton.onclick = ()=> {
    dropDownMenu.classList.toggle('open')
}