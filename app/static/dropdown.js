var dropdown = document.getElementsByClassName("dropdown")[0]
var dropdown_ul_ = document.getElementsByClassName("dropdown_ul")[0]




dropdown.addEventListener("mousemove", function () {

    dropdown_ul_.classList.add("dropdown_ul_shown")

})
dropdown.addEventListener("mouseleave", function () {
   
    dropdown_ul_.classList.remove("dropdown_ul_shown")

    
})
dropdown_ul_.addEventListener("mousemove", function () {

    dropdown_ul_.classList.add("dropdown_ul_shown")

})
dropdown_ul_.addEventListener("mouseleave", function () {
  
    dropdown_ul_.classList.remove("dropdown_ul_shown")
    
})
