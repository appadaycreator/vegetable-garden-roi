# ★このサービスの独自コンテキスト（品質向上のため必ず参照）:
# 解決する問題: 栽培する野菜・面積・初期投資から年間の節約額と収益化可能性を計算
# 対象ユーザー: 賢くお金を管理したい家庭
# キーワード: 家庭菜園
TITLE = '家庭菜園コスト・収益計算【無料】無料Webツール'
DESCRIPTION = '栽培する野菜・面積・初期投資から年間の節約額と収益化可能性を計算。登録不要・完全無料でご利用いただけます。'
DESCRIPTION_SHORT = '栽培する野菜・面積・初期投資から年間の節約額と収益化可能性を計算。'
COLOR1 = '#E0E7FF'
COLOR2 = '#F0F4FF'
COLOR_BTN = '#6366F1'
FOOTER_LINKS = [('https://appadaycreator.com/vegetable-garden-calendar/', '🌱 家庭菜園カレンダー'), ('https://appadaycreator.com/garden-planting-calendar/', '家庭菜園・植付けカレンダー'), ('https://appadaycreator.com/recipe-scaling-calculator/', 'レシピ量調整計算ツール')]

CUSTOM_CSS = """"""

# MAIN_HTML≤100行 / 色=#6366F1 / class="card"でUI / id="result"で結果隠し
MAIN_HTML = """<div class="card">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:16px;">🥕 家庭菜園ROI・節約額計算</h2>
  <label>栽培スペース（㎡）</label>
  <input type="number" id="area" placeholder="例: 2" min="0.5" max="100" step="0.5">
  <label>主に育てる野菜</label>
  <select id="crop">
    <option value="tomato">トマト・ミニトマト</option>
    <option value="leafy">葉物野菜（レタス・ほうれん草）</option>
    <option value="herb">ハーブ（バジル・パセリ）</option>
    <option value="cucumber">きゅうり・なす</option>
    <option value="root">根菜（大根・じゃがいも）</option>
  </select>
  <label>初期投資額（円）苗・土・プランター代等</label>
  <input type="number" id="initial" placeholder="例: 15000" min="0" step="1000">
  <label>月間の手入れ時間（時間）</label>
  <input type="number" id="hours" placeholder="例: 4" min="0.5" max="100" step="0.5">
  <button class="btn" style="margin-top:20px;" onclick="generate()">ROIを計算する</button>
</div>
<div class="result" id="result" style="margin-top:16px;">
  <div class="card">
    <h3 style="font-size:15px;font-weight:700;margin-bottom:12px;color:#6366F1;">📊 家庭菜園 収支レポート</h3>
    <div id="output"></div>
  </div>
</div>"""

# JS: スタブの TODO コメント箇所を実装してください（骨格は変えないこと）
JS_CODE = """const CROPS = {
  tomato:   { name:'トマト・ミニトマト', yieldPerSqm:4, pricePerKg:400, months:5 },
  leafy:    { name:'葉物野菜', yieldPerSqm:6, pricePerKg:300, months:8 },
  herb:     { name:'ハーブ', yieldPerSqm:2, pricePerKg:2000, months:6 },
  cucumber: { name:'きゅうり・なす', yieldPerSqm:5, pricePerKg:250, months:4 },
  root:     { name:'根菜', yieldPerSqm:3, pricePerKg:150, months:4 },
};
function getInputs() {
  const area = parseFloat(document.getElementById('area').value);
  const initial = parseInt(document.getElementById('initial').value);
  const hours = parseFloat(document.getElementById('hours').value);
  if(!area || !initial || !hours) { alert('全ての項目を入力してください'); return null; }
  return { area, crop: document.getElementById('crop').value, initial, hours };
}
function buildOutput(inputs) {
  const { area, crop, initial, hours } = inputs;
  const c = CROPS[crop];
  const annualYield = c.yieldPerSqm * area * c.months;
  const annualSaving = Math.round(annualYield * c.pricePerKg);
  const paybackMonths = Math.ceil(initial / (annualSaving / 12));
  const roi = Math.round((annualSaving - initial) / initial * 100);
  const laborCost = Math.round(hours * 12 * 1000);
  const netBenefit = annualSaving - (initial > 0 ? initial / 3 : 0);
  const emoji = roi > 100 ? '🏆' : roi > 0 ? '✅' : '⚠️';
  return `<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px;">
    <div style="background:#eff6ff;border-radius:10px;padding:14px;text-align:center;">
      <div style="font-size:11px;color:#6b7280;">年間節約額</div>
      <div style="font-size:22px;font-weight:700;color:#2563eb;">${annualSaving.toLocaleString()}円</div>
    </div>
    <div style="background:#f0fdf4;border-radius:10px;padding:14px;text-align:center;">
      <div style="font-size:11px;color:#6b7280;">初期費用回収</div>
      <div style="font-size:22px;font-weight:700;color:#16a34a;">${paybackMonths}ヶ月</div>
    </div>
  </div>
  <div style="background:#fafafa;border-radius:10px;padding:14px;font-size:13px;color:#374151;line-height:2;">
    ${emoji} ROI（投資対効果）: <strong>${roi}%</strong><br>
    🌱 ${c.name} ${area}㎡ → 年間収穫量 約${annualYield.toFixed(1)}kg<br>
    ⏰ 年間作業時間: ${(hours*12).toFixed(0)}時間（時給換算 ${Math.round(annualSaving/(hours*12))}円/h）<br>
    💡 ${roi > 50 ? 'コスパ良好！継続的な投資を検討してください' : roi > 0 ? '採算は取れています。規模を拡大するとROIが向上します' : 'ハーブ・葉物野菜に切り替えると収益性が改善します'}
  </div>`;
}
document.addEventListener('DOMContentLoaded',()=>{});
function generate() {
  const inputs = getInputs(); if(!inputs) return;
  document.getElementById('output').innerHTML = buildOutput(inputs);
  document.getElementById('result').classList.add('show');
  document.getElementById('result').scrollIntoView({behavior:'smooth',block:'start'});
}"""

FAQ = [
    ("家庭菜園コスト・収益計算は無料で使えますか？", "はい、完全無料・登録不要でご利用いただけます。"),
    ("何回でも使えますか？", "はい、回数制限なく何度でもご利用いただけます。"),
    ("入力したデータはサーバーに送信されますか？", "いいえ。すべての処理はブラウザ内で完結し、入力内容はサーバーへ送信されません。"),
    ("スマートフォンでも使えますか？", "はい、スマートフォン・タブレット・PCすべてに最適化されています。"),
    ("結果を保存・共有できますか？", "スクリーンショットでの保存またはSNSシェアボタンからご共有いただけます。"),
]

HOW_TO = [
    "ページを開き、入力フォームの項目を確認する",
    "必要な情報を入力または選択する",
    "実行ボタンをクリックして結果を取得する",
    "表示された結果・アドバイスを確認する",
    "必要に応じてコピー・SNSシェアで活用する",
]

