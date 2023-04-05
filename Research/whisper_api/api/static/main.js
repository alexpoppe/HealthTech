document.querySelector('textarea').addEventListener("input", function(){
    this.style.height = '0px';
    this.style.height = this.scrollHeight + 'px';
})
