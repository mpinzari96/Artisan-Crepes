// Accessible mobile nav toggle (<1 KB). aria-expanded, Escape closes, link click closes.
(function(){
  var b=document.querySelector('.nav-toggle'),n=document.getElementById('primary-nav');
  if(!b||!n)return;
  function set(o){n.classList.toggle('is-open',o);b.setAttribute('aria-expanded',o?'true':'false');b.textContent=o?'Close':'Menu';}
  b.addEventListener('click',function(){set(b.getAttribute('aria-expanded')!=='true')});
  n.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&b.getAttribute('aria-expanded')==='true'){set(false);b.focus();}});
  var d=document.getElementById('pd');
  if(d){var t=new Date();t.setDate(t.getDate()+3);d.min=t.toISOString().slice(0,10);} // 72-hr lead time (placeholder)
})();
