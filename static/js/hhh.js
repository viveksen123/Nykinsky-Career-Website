const open=document.getElementsById('open');
const model_container=document.getElementById(modal_container);
const OK=document.getElementById('OK');

open.addEventListener('Click',()=> {
    modal_container.classList.add('show');
});
OK.addEventListener('click',()=>{
    modal_container.classList.remove('show');
});
