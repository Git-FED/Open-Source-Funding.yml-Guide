const feeModels = [
  {name:'GitHub Sponsors', fee:0, note:'personal orientation', color:100},
  {name:'Ko-fi tips', fee:3.2, note:'processor orientation', color:96.8},
  {name:'Liberapay', fee:3.2, note:'processor orientation', color:96.8},
  {name:'Buy Me a Coffee', fee:8.2, note:'platform + processor', color:91.8},
  {name:'Polar', fee:8.6, note:'platform + processor + fixed', color:91.4},
  {name:'Open Collective', fee:10.5, note:'host + processor midpoint', color:89.5},
  {name:'Patreon', fee:12.5, note:'plan + processor midpoint', color:87.5},
  {name:'IssueHunt', fee:20, note:'bounty orientation', color:80}
];
const amount = document.querySelector('#amount');
const results = document.querySelector('#results');
function render(){
  const value = Math.max(1, Number(amount.value) || 100);
  results.innerHTML = feeModels.map(item => {
    const keep = value * (1 - item.fee / 100);
    return `<div class="result"><div><span class="result-name">${item.name}</span><span class="result-note">${item.note} · ${item.fee}% model</span></div><span class="result-value">$${keep.toFixed(2)}</span><div class="bar"><span style="width:${item.color}%"></span></div></div>`;
  }).join('');
}
amount.addEventListener('input', render); render();
