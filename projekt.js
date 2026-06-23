/* ============ Projekt-Detailseite ============ */
(function(){
  /* scroll reveal */
  const io=new IntersectionObserver(es=>{
    es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});
  },{threshold:.14,rootMargin:'0px 0px -8% 0px'});
  document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

  /* gallery lightbox */
  const items=[...document.querySelectorAll('.gal-item')];
  const lb=document.getElementById('lb');
  if(lb&&items.length){
    const lbImg=document.getElementById('lbImg'),lbCount=document.getElementById('lbCount');
    const lbBtns=[...lb.querySelectorAll('.lb-btn')];
    let idx=0,lastFocus=null;
    const fill=i=>{
      idx=(i+items.length)%items.length;
      const it=items[idx];
      lbImg.src=it.dataset.full||it.querySelector('img').src;
      lbImg.alt=it.querySelector('img').alt||'';
      lbCount.textContent=(idx+1)+' / '+items.length;
    };
    const open=i=>{
      lastFocus=document.activeElement;fill(i);
      lb.classList.add('open');lb.setAttribute('aria-hidden','false');
      document.body.style.overflow='hidden';
      requestAnimationFrame(()=>lb.classList.add('show'));
      document.getElementById('lbClose').focus();
    };
    const close=()=>{
      lb.classList.remove('show');lb.setAttribute('aria-hidden','true');
      document.body.style.overflow='';
      setTimeout(()=>lb.classList.remove('open'),350);
      if(lastFocus)lastFocus.focus();
    };
    items.forEach((it,i)=>it.addEventListener('click',()=>open(i)));
    document.getElementById('lbClose').addEventListener('click',close);
    document.getElementById('lbPrev').addEventListener('click',()=>fill(idx-1));
    document.getElementById('lbNext').addEventListener('click',()=>fill(idx+1));
    lb.addEventListener('click',e=>{if(e.target===lb)close();});
    addEventListener('keydown',e=>{
      if(!lb.classList.contains('open'))return;
      if(e.key==='Escape')close();
      else if(e.key==='ArrowLeft')fill(idx-1);
      else if(e.key==='ArrowRight')fill(idx+1);
      else if(e.key==='Tab'){
        const f=lbBtns,first=f[0],last=f[f.length-1];
        if(e.shiftKey&&document.activeElement===first){e.preventDefault();last.focus();}
        else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first.focus();}
        else if(!f.includes(document.activeElement)){e.preventDefault();first.focus();}
      }
    });
  }

  /* before/after slider */
  document.querySelectorAll('.ba').forEach(ba=>{
    const range=ba.querySelector('.ba-range');
    const set=v=>{v=Math.max(0,Math.min(100,v));ba.style.setProperty('--pos',v+'%');if(range)range.value=v;};
    const fromX=x=>{const r=ba.getBoundingClientRect();return ((x-r.left)/r.width)*100;};
    let drag=false;
    ba.addEventListener('pointerdown',e=>{drag=true;ba.setPointerCapture(e.pointerId);set(fromX(e.clientX));});
    ba.addEventListener('pointermove',e=>{if(drag)set(fromX(e.clientX));});
    ['pointerup','pointercancel'].forEach(ev=>ba.addEventListener(ev,()=>drag=false));
    if(range)range.addEventListener('input',()=>set(+range.value));
    set(range?+range.value:50);
  });

  /* Farbwelt-Umschalter (seitenübergreifend) */
  const sw=document.querySelector('.theme-switch');
  if(sw){
    const tbtns=[...sw.querySelectorAll('.tsw')];
    const meta=document.querySelector('meta[name="theme-color"]');
    const dark={holz:'#1b1409',schiefer:'#222a30',kalk:'#2b3127'};
    const reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
    const paint=name=>{
      tbtns.forEach(b=>b.setAttribute('aria-pressed', b.dataset.themeSet===name?'true':'false'));
      if(meta)meta.setAttribute('content', dark[name]||'#1b1409');
    };
    const setTheme=name=>{
      const apply=()=>{
        if(name==='holz')delete document.documentElement.dataset.theme; else document.documentElement.dataset.theme=name;
        try{localStorage.setItem('aigner-theme',name);}catch(e){}
        paint(name);
      };
      if(document.startViewTransition&&!reduce){document.startViewTransition(apply);}else{apply();}
    };
    tbtns.forEach(b=>b.addEventListener('click',()=>setTheme(b.dataset.themeSet)));
    paint(document.documentElement.dataset.theme||'holz');
  }

  /* year */
  const yr=document.getElementById('yr');if(yr)yr.textContent=new Date().getFullYear();
})();
