<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>未来ルートナビ | あなたにぴったりの系列・コース診断</title>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <!-- Google Fonts: Zen Maru Gothic & Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@600;700;800&family=Zen+Maru+Gothic:wght@500;700;900&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Zen Maru Gothic"', '"Plus Jakarta Sans"', 'sans-serif'],
          },
          colors: {
            brand: {
              pink: '#FF6B9B',
              purple: '#8B5CF6',
              cyan: '#06B6D4',
              yellow: '#FACC15',
              dark: '#0F172A',
            }
          },
          animation: {
            'bounce-slow': 'bounce 3s infinite',
            'pulse-glow': 'pulseGlow 2s infinite alternate',
            'float': 'float 4s ease-in-out infinite',
          },
          keyframes: {
            pulseGlow: {
              '0%': { boxShadow: '0 0 15px rgba(255, 107, 155, 0.4)' },
              '100%': { boxShadow: '0 0 30px rgba(139, 92, 246, 0.8)' },
            },
            float: {
              '0%, 100%': { transform: 'translateY(0px)' },
              '50%': { transform: 'translateY(-10px)' },
            }
          }
        }
      }
    }
  </script>

  <style>
    /* グラスモフィズムスタイル */
    .glass-card {
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 2px solid rgba(255, 255, 255, 0.6);
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
    }
    .glass-card-dark {
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* 背景グラデーション */
    body {
      background: linear-gradient(135deg, #FFF1F5 0%, #E0E7FF 50%, #E0F2FE 100%);
      min-height: 100vh;
    }

    /* 吹き出しの三角形 */
    .speech-bubble::before {
      content: '';
      position: absolute;
      left: -12px;
      top: 24px;
      width: 0;
      height: 0;
      border-top: 10px solid transparent;
      border-bottom: 10px solid transparent;
      border-right: 14px solid white;
      filter: drop-shadow(-2px 0 2px rgba(0,0,0,0.05));
    }

    @media (max-width: 640px) {
      .speech-bubble::before {
        left: 28px;
        top: -12px;
        border-left: 10px solid transparent;
        border-right: 10px solid transparent;
        border-bottom: 14px solid white;
        border-top: none;
      }
    }

    /* カスタムスクロールバー */
    ::-webkit-scrollbar {
      width: 8px;
    }
    ::-webkit-scrollbar-track {
      background: rgba(0,0,0,0.05);
    }
    ::-webkit-scrollbar-thumb {
      background: #8B5CF6;
      border-radius: 4px;
    }
  </style>
</head>
<body class="text-slate-800 font-sans p-3 sm:p-6 flex flex-col justify-between items-center min-h-screen">

  <!-- ヘッダー -->
  <header class="w-full max-w-3xl flex justify-between items-center mb-4 px-2">
    <div class="flex items-center gap-2">
      <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-brand-pink to-brand-purple flex items-center justify-center text-white shadow-lg text-xl font-black">
        ✦
      </div>
      <span class="font-black text-xl bg-clip-text text-transparent bg-gradient-to-r from-brand-pink via-brand-purple to-brand-cyan">
        未来ルートナビ
      </span>
    </div>
    <div class="flex items-center gap-2">
      <!-- SNS/Instagramクイックリンクボタン -->
      <button onclick="toggleSnsSidebar()" class="text-xs font-bold text-slate-700 bg-white/90 hover:bg-white backdrop-blur-md px-3 py-1.5 rounded-full border border-pink-200 shadow-sm flex items-center gap-1.5 transition-all">
        <i class="fa-brands fa-instagram text-pink-500 text-sm"></i>
        <span class="hidden sm:inline">公式・部活</span>SNS
      </button>
      <div class="text-xs font-bold text-purple-600 bg-white/80 backdrop-blur-md px-3 py-1.5 rounded-full border border-purple-200 shadow-sm hidden sm:block">
        <i class="fa-solid fa-sparkles text-brand-pink mr-1"></i> 高校生向けコース・系列診断
      </div>
    </div>
  </header>

  <!-- メインコンテンツカード -->
  <main class="w-full max-w-3xl flex-1 flex flex-col justify-center">

    <!-- 1. スタート画面 -->
    <div id="screen-start" class="glass-card rounded-3xl p-6 sm:p-8 text-center animate-float">
      <!-- キャラクター紹介 -->
      <div class="relative w-32 h-32 mx-auto mb-4">
        <div class="absolute inset-0 bg-gradient-to-r from-pink-300 via-purple-300 to-cyan-300 rounded-full animate-pulse-glow"></div>
        <!-- キャラ画像 (SVGプレースホルダー) -->
        <div id="start-mascot" class="relative z-10 w-full h-full flex items-center justify-center">
          <!-- キャラクターSVG -->
          <svg viewBox="0 0 100 100" class="w-28 h-28 drop-shadow-md">
            <circle cx="50" cy="50" r="45" fill="#FFE4E6"/>
            <circle cx="50" cy="50" r="38" fill="#FFF"/>
            <!-- 髪型 -->
            <path d="M 25 45 C 25 20, 75 20, 75 45 Z" fill="#8B5CF6"/>
            <circle cx="28" cy="40" r="8" fill="#8B5CF6"/>
            <circle cx="72" cy="40" r="8" fill="#8B5CF6"/>
            <!-- 目 -->
            <circle cx="38" cy="48" r="4" fill="#0F172A"/>
            <circle cx="62" cy="48" r="4" fill="#0F172A"/>
            <circle cx="40" cy="46" r="1.5" fill="#FFF"/>
            <circle cx="64" cy="46" r="1.5" fill="#FFF"/>
            <!-- ほっぺ -->
            <ellipse cx="33" cy="54" rx="4" ry="2.5" fill="#FF6B9B" opacity="0.6"/>
            <ellipse cx="67" cy="54" rx="4" ry="2.5" fill="#FF6B9B" opacity="0.6"/>
            <!-- 口 (にっこり) -->
            <path d="M 43 56 Q 50 63 57 56" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none"/>
          </svg>
        </div>
      </div>

      <h1 class="text-2xl sm:text-4xl font-black text-slate-800 mb-3 tracking-tight">
        キミにピッタリの<br class="sm:hidden"><span class="bg-gradient-to-r from-brand-pink to-brand-purple bg-clip-text text-transparent">高校の系列・コース</span>を探そう！
      </h1>
      <p class="text-sm sm:text-base text-slate-600 mb-6 max-w-md mx-auto leading-relaxed">
        ナビゲーターの「ナビィ」だよ！直感的な質問に答えるだけで、あなたの得意や興味に合ったコースを分析するよ✨
      </p>

      <!-- メイン診断ボタン -->
      <button onclick="startApp()" class="w-full sm:w-auto px-10 py-4 bg-gradient-to-r from-brand-pink via-brand-purple to-brand-cyan text-white text-lg font-black rounded-2xl shadow-xl hover:opacity-95 hover:scale-105 transition-all duration-300 flex items-center justify-center gap-3 mx-auto mb-6">
        <span>診断をはじめる</span>
        <i class="fa-solid fa-arrow-right"></i>
      </button>

      <!-- 説明モーダル起動ボタンエリア -->
      <div class="flex flex-wrap items-center justify-center gap-3 pt-4 border-t border-slate-200/60">
        <button onclick="openSchoolModal()" class="px-4 py-2 bg-white/90 hover:bg-white text-purple-700 text-xs sm:text-sm font-bold rounded-xl border border-purple-200 shadow-sm transition-all flex items-center gap-2">
          <i class="fa-solid fa-school text-purple-500"></i>
          <span>KIKSの説明を見る</span>
        </button>
        <button onclick="openTracksListModal()" class="px-4 py-2 bg-white/90 hover:bg-white text-pink-700 text-xs sm:text-sm font-bold rounded-xl border border-pink-200 shadow-sm transition-all flex items-center gap-2">
          <i class="fa-solid fa-layer-group text-pink-500"></i>
          <span>各系列の説明を見る</span>
        </button>
      </div>
    </div>

    <!-- 2. 進路分岐選択画面 -->
    <div id="screen-branch" class="hidden glass-card rounded-3xl p-6 sm:p-8 text-center space-y-6">
      <div class="w-20 h-20 mx-auto rounded-2xl bg-white p-2 shadow-md border-2 border-purple-200 flex items-center justify-center">
        <svg viewBox="0 0 100 100" class="w-full h-full drop-shadow">
          <circle cx="50" cy="50" r="42" fill="#F3E8FF"/>
          <path d="M 25 45 C 25 20, 75 20, 75 45 Z" fill="#8B5CF6"/>
          <circle cx="28" cy="40" r="8" fill="#8B5CF6"/>
          <circle cx="72" cy="40" r="8" fill="#8B5CF6"/>
          <circle cx="38" cy="48" r="4" fill="#0F172A"/>
          <circle cx="62" cy="48" r="4" fill="#0F172A"/>
          <ellipse cx="33" cy="53" rx="4" ry="2.5" fill="#FF6B9B" opacity="0.6"/>
          <ellipse cx="67" cy="53" rx="4" ry="2.5" fill="#FF6B9B" opacity="0.6"/>
          <ellipse cx="50" cy="58" rx="6" ry="5" fill="#0F172A"/>
        </svg>
      </div>

      <div class="speech-bubble relative glass-card p-5 rounded-2xl border-2 border-white max-w-lg mx-auto">
        <p id="branch-text" class="text-base sm:text-lg font-bold text-slate-800 leading-snug"></p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 pt-2 max-w-lg mx-auto">
        <button onclick="selectBranch(true)" class="p-5 rounded-2xl bg-white/90 hover:bg-purple-600 hover:text-white border-2 border-purple-200 shadow-sm transition-all text-left group flex flex-col justify-between h-full">
          <div>
            <div class="font-extrabold text-base mb-1 group-hover:text-white text-slate-800">はい！決まっている✨</div>
            <p class="text-xs text-slate-500 group-hover:text-purple-100">目的の学部・分野から最適な系列をピンポイントで案内します。</p>
          </div>
          <div class="mt-4 text-right">
            <i class="fa-solid fa-arrow-right text-purple-500 group-hover:text-white"></i>
          </div>
        </button>

        <button onclick="selectBranch(false)" class="p-5 rounded-2xl bg-white/90 hover:bg-pink-500 hover:text-white border-2 border-pink-200 shadow-sm transition-all text-left group flex flex-col justify-between h-full">
          <div>
            <div class="font-extrabold text-base mb-1 group-hover:text-white text-slate-800">まだ探している！🤔</div>
            <p class="text-xs text-slate-500 group-hover:text-pink-100">8つの性格・適性質問に答えて相性の良いコースを見つけます。</p>
          </div>
          <div class="mt-4 text-right">
            <i class="fa-solid fa-arrow-right text-pink-500 group-hover:text-white"></i>
          </div>
        </button>
      </div>
    </div>


    <!-- 3. クイズ進行画面 (MBTI風 or 進路決定ルート) -->
    <div id="screen-quiz" class="hidden space-y-5">
      <!-- プログレスバー -->
      <div class="space-y-1">
        <div class="flex justify-between items-center text-xs font-black text-slate-500 px-1">
          <span id="quiz-progress-text">QUESTION 1 / 8</span>
          <span id="quiz-progress-percent" class="text-purple-600">12%</span>
        </div>
        <div class="w-full h-3 bg-white/70 rounded-full overflow-hidden p-0.5 border border-white">
          <div id="quiz-progress-bar" class="h-full bg-gradient-to-r from-brand-pink to-brand-purple rounded-full transition-all duration-300 w-0"></div>
        </div>
      </div>

      <!-- キャラクター＆質問吹き出し -->
      <div class="flex flex-col sm:flex-row items-center sm:items-start gap-4">
        <!-- キャラクター (表情チェンジ対応) -->
        <div class="relative shrink-0">
          <div class="w-20 h-20 sm:w-24 sm:h-24 rounded-2xl bg-white p-2 shadow-md border-2 border-purple-200 flex items-center justify-center">
            <div id="quiz-mascot-avatar" class="w-full h-full">
              <!-- JSで動的に表情が変化 -->
            </div>
          </div>
          <span class="absolute -bottom-2 left-1/2 -translate-x-1/2 bg-purple-600 text-white text-[10px] font-extrabold px-2 py-0.5 rounded-full whitespace-nowrap">ナビィ</span>
        </div>

        <!-- 質問の吹き出し -->
        <div class="speech-bubble relative glass-card p-5 rounded-2xl flex-1 w-full border-2 border-white min-h-[90px] flex items-center">
          <p id="quiz-question-text" class="text-base sm:text-lg font-bold text-slate-800 leading-snug"></p>
        </div>
      </div>

      <!-- 選択肢リスト -->
      <div id="quiz-options-container" class="space-y-3 pt-2">
        <!-- JSで動的生成 -->
      </div>
    </div>


    <!-- 4. 診断結果画面 -->
    <div id="screen-result" class="hidden space-y-6">
      
      <!-- トップカード: マッチした系列 -->
      <div class="glass-card rounded-3xl p-6 sm:p-8 text-center border-2 border-white relative overflow-hidden">
        <!-- 背景装飾 -->
        <div class="absolute -top-12 -right-12 w-36 h-36 bg-purple-200/50 rounded-full blur-2xl"></div>
        <div class="absolute -bottom-12 -left-12 w-36 h-36 bg-pink-200/50 rounded-full blur-2xl"></div>

        <span class="inline-block px-4 py-1.5 rounded-full bg-gradient-to-r from-brand-pink to-brand-purple text-white text-xs font-black tracking-wider uppercase shadow-sm mb-3">
          ✦ 診断結果 ✦
        </span>

        <h2 class="text-xs sm:text-sm font-bold text-slate-500">あなたと最も相性が良い高校のコースは...</h2>
        
        <!-- 系列タイトル -->
        <div id="result-title" class="text-2xl sm:text-4xl font-black text-slate-800 my-3">
          <!-- JSで挿入 -->
        </div>

        <!-- マッチ度ゲージ -->
        <div class="max-w-xs mx-auto my-4 bg-white/80 p-3 rounded-2xl border border-purple-100 shadow-inner">
          <div class="flex justify-between text-xs font-black text-slate-600 mb-1">
            <span>あなたとの適性マッチ度</span>
            <span id="result-match-score" class="text-purple-600 text-sm">95%</span>
          </div>
          <div class="w-full bg-slate-100 rounded-full h-3 overflow-hidden">
            <div id="result-match-bar" class="bg-gradient-to-r from-pink-500 to-purple-600 h-full rounded-full transition-all duration-1000 w-0"></div>
          </div>
        </div>

        <!-- キャラクターのコメント -->
        <div class="flex items-center gap-3 bg-white/90 p-4 rounded-2xl border border-purple-100 text-left my-4 shadow-sm">
          <div class="w-12 h-12 shrink-0 rounded-xl bg-purple-100 p-1 flex items-center justify-center">
            <svg viewBox="0 0 100 100" class="w-full h-full">
              <circle cx="50" cy="50" r="40" fill="#FFF"/>
              <path d="M 25 45 C 25 20, 75 20, 75 45 Z" fill="#8B5CF6"/>
              <circle cx="38" cy="48" r="4" fill="#0F172A"/>
              <circle cx="62" cy="48" r="4" fill="#0F172A"/>
              <path d="M 42 58 Q 50 66 58 58" stroke="#0F172A" stroke-width="3" stroke-linecap="round" fill="none"/>
            </svg>
          </div>
          <p id="result-mascot-comment" class="text-xs sm:text-sm font-bold text-slate-700 leading-relaxed"></p>
        </div>
      </div>

      <!-- 詳細解説カード -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- 特徴・性格傾向 -->
        <div class="glass-card p-5 rounded-2xl border-2 border-white">
          <h3 class="font-extrabold text-base text-slate-800 flex items-center gap-2 mb-3">
            <i class="fa-solid fa-sparkles text-brand-pink"></i> あなたの強み・特徴
          </h3>
          <ul id="result-traits" class="space-y-2 text-xs sm:text-sm text-slate-600">
            <!-- JSで動的挿入 -->
          </ul>
        </div>

        <!-- 将来の進路・適性学部 -->
        <div class="glass-card p-5 rounded-2xl border-2 border-white">
          <h3 class="font-extrabold text-base text-slate-800 flex items-center gap-2 mb-3">
            <i class="fa-solid fa-compass text-brand-cyan"></i> 目指せる大学学部・将来の職種
          </h3>
          <div class="space-y-3 text-xs sm:text-sm">
            <div>
              <span class="font-black text-slate-500 text-[11px] block mb-1">【おすすめ学部】</span>
              <div id="result-faculties" class="flex flex-wrap gap-1.5">
                <!-- JSでバッジ生成 -->
              </div>
            </div>
            <div>
              <span class="font-black text-slate-500 text-[11px] block mb-1">【向いている職種】</span>
              <div id="result-careers" class="flex flex-wrap gap-1.5">
                <!-- JSでバッジ生成 -->
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- アクションボタン -->
      <div class="flex flex-col sm:flex-row gap-3 pt-2">
        <button onclick="restartApp()" class="flex-1 py-3.5 px-6 bg-white hover:bg-slate-50 text-slate-700 font-extrabold rounded-2xl border-2 border-slate-200 transition-all flex items-center justify-center gap-2 shadow-sm">
          <i class="fa-solid fa-rotate-right"></i>
          <span>もう一度診断する</span>
        </button>
      <!-- 全系列詳細リスト表示用モーダル -->
      <div id="modal-all-tracks" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="glass-card max-w-2xl w-full max-h-[85vh] rounded-3xl p-6 overflow-y-auto space-y-4">
          <div class="flex justify-between items-center border-b pb-3">
            <h3 class="font-black text-lg text-slate-800">すべての系列・コース一覧</h3>
            <button onclick="toggleAllTracksModal()" class="w-8 h-8 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 font-bold hover:bg-slate-200">✕</button>
          </div>
          <div id="modal-tracks-list" class="space-y-3">
            <!-- JSで動的生成 -->
          </div>
        </div>
      </div>

    </div>

  </main>

  <!-- フッター -->
  <footer class="w-full max-w-3xl text-center py-4 text-xs font-medium text-slate-400">
    &copy; 未来ルートナビ - 高校生のための進路・系列診断アプリ
  </footer>

  <!-- 1. Instagram / SNSサイドバー -->
  <div id="sidebar-sns" class="fixed inset-y-0 right-0 w-72 bg-white/95 backdrop-blur-md z-50 shadow-2xl transform translate-x-full transition-transform duration-300 ease-in-out p-5 flex flex-col justify-between border-l border-slate-100">
    <div>
      <div class="flex items-center justify-between pb-4 border-b border-slate-100">
        <h3 class="font-black text-slate-800 text-base flex items-center gap-2">
          <i class="fa-brands fa-instagram text-pink-500 text-xl"></i>
          公式・部活 Instagram
        </h3>
        <button onclick="toggleSnsSidebar()" class="w-8 h-8 rounded-full bg-slate-100 text-slate-500 flex items-center justify-center hover:bg-slate-200 font-bold">✕</button>
      </div>
      <p class="text-xs text-slate-500 mt-3 mb-4 leading-relaxed">
        学校の雰囲気や部活動の日常をInstagramでチェックしよう！
      </p>
      <div class="space-y-3">
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="flex items-center gap-3 p-3 rounded-2xl bg-gradient-to-r from-purple-50 to-pink-50 hover:from-purple-100 hover:to-pink-100 border border-pink-100 transition-all">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-yellow-400 via-pink-500 to-purple-600 text-white flex items-center justify-center text-lg shadow-sm">
            <i class="fa-brands fa-instagram"></i>
          </div>
          <div>
            <div class="font-black text-xs text-slate-800">学校公式 Instagram</div>
            <div class="text-[10px] text-slate-500">@kiks_official</div>
          </div>
        </a>
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="flex items-center gap-3 p-3 rounded-2xl bg-slate-50 hover:bg-slate-100 border border-slate-200/60 transition-all">
          <div class="w-10 h-10 rounded-xl bg-pink-500 text-white flex items-center justify-center text-lg shadow-sm">
            <i class="fa-solid fa-trophy"></i>
          </div>
          <div>
            <div class="font-black text-xs text-slate-800">運動部公式アカウント</div>
            <div class="text-[10px] text-slate-500">部活動の最新大会結果など</div>
          </div>
        </a>
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="flex items-center gap-3 p-3 rounded-2xl bg-slate-50 hover:bg-slate-100 border border-slate-200/60 transition-all">
          <div class="w-10 h-10 rounded-xl bg-purple-500 text-white flex items-center justify-center text-lg shadow-sm">
            <i class="fa-solid fa-palette"></i>
          </div>
          <div>
            <div class="font-black text-xs text-slate-800">文化部・生徒会</div>
            <div class="text-[10px] text-slate-500">学校行事・作品展示など</div>
          </div>
        </a>
      </div>
    </div>
    <div class="text-[11px] text-slate-400 text-center">
      ※タップするとInstagramアプリまたはブラウザが開きます
    </div>
  </div>

  <!-- 2. KIKS学校説明モーダル -->
  <div id="modal-school-info" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-3 sm:p-6">
    <div class="glass-card w-full h-full max-w-3xl rounded-3xl p-6 sm:p-8 overflow-y-auto space-y-6 flex flex-col justify-between">
      <div>
        <div class="flex justify-between items-center border-b pb-4 mb-4">
          <h3 class="font-black text-xl sm:text-2xl text-slate-800 flex items-center gap-2">
            <span class="w-8 h-8 rounded-xl bg-purple-600 text-white flex items-center justify-center text-xs">✦</span>
            KIKSについて
          </h3>
          <button onclick="closeSchoolModal()" class="w-9 h-9 rounded-full bg-slate-100 flex items-center justify-center text-slate-500 font-bold hover:bg-slate-200 transition-all">✕</button>
        </div>
        <div class="space-y-4 text-sm sm:text-base text-slate-700 leading-relaxed">
          <div class="p-5 rounded-2xl bg-purple-50 border border-purple-100">
            <h4 class="font-black text-purple-900 text-lg mb-2">未来を切り拓く多様な学び</h4>
            <p class="text-slate-600 leading-relaxed">
              KIKSでは、一人ひとりの個性や将来の夢に合わせた多角的なカリキュラムを展開しています。文系・理系の枠にとらわれず、最新のテクノロジー、地域創生、防災、ダイバーシティなど、自分の「好き」を突き詰めることができる環境が整っています。
            </p>
          </div>
          <div>
            <h5 class="font-extrabold text-slate-800 mb-3 flex items-center gap-2 text-base">
              <i class="fa-solid fa-star text-amber-400"></i> KIKSの3つの魅力
            </h5>
            <ul class="space-y-3">
              <li class="flex items-start gap-3 bg-white/80 p-4 rounded-2xl border border-slate-100 shadow-sm">
                <span class="font-black text-purple-600 text-lg">01</span>
                <div>
                  <strong>特長豊かな系列群：</strong> 自分の適性に合わせて主体的に深掘りできる多彩なコース設計。
                </div>
              </li>
              <li class="flex items-start gap-3 bg-white/80 p-4 rounded-2xl border border-slate-100 shadow-sm">
                <span class="font-black text-purple-600 text-lg">02</span>
                <div>
                  <strong>地域・社会連携：</strong> ひょうご・地域社会や企業と連携した探究型プロジェクト学習。
                </div>
              </li>
              <li class="flex items-start gap-3 bg-white/80 p-4 rounded-2xl border border-slate-100 shadow-sm">
                <span class="font-black text-purple-600 text-lg">03</span>
                <div>
                  <strong>一人ひとりの進路実現：</strong> 総合型選抜から一般入試、就職まで個別に手厚いサポートを実施。
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="pt-4 border-t border-slate-200/60 text-center">
        <button onclick="closeSchoolModal()" class="w-full sm:w-auto px-10 py-3.5 bg-slate-800 hover:bg-slate-900 text-white font-extrabold rounded-2xl transition-all shadow-md">
          閉じる
        </button>
      </div>
    </div>
  </div>

  <!-- 3. 各系列の説明選択モーダル -->
  <div id="modal-tracks-selector" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-3 sm:p-6">
    <div class="glass-card w-full h-full max-w-3xl rounded-3xl p-5 sm:p-8 overflow-y-auto space-y-4 flex flex-col justify-between">
      <div>
        <div class="flex justify-between items-center border-b pb-3 mb-4">
          <div class="flex items-center gap-2">
            <div>
              <h3 class="font-black text-lg sm:text-2xl text-slate-800">系列・コースの詳細説明</h3>
              <p class="text-xs sm:text-sm text-slate-500">気になる系列を選んで説明を表示します</p>
            </div>
          </div>
          <button onclick="closeTracksListModal()" class="w-9 h-9 rounded-full bg-slate-100 text-slate-500 flex items-center justify-center font-bold hover:bg-slate-200 transition-all">✕</button>
        </div>

        <!-- 8系列ボタン一覧 -->
        <div id="tracks-button-grid" class="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-4">
          <!-- JSで動的にボタン生成 -->
        </div>

        <!-- 選択された系列の詳細表示領域 -->
        <div id="track-detail-display" class="pt-3 border-t border-slate-200/60">
          <!-- JSで選択結果を動的表示 -->
        </div>
      </div>

      <!-- 下部固定閉じるボタン -->
      <div class="pt-4 border-t border-slate-200/60 text-center">
        <button onclick="closeTracksListModal()" class="w-full sm:w-auto px-10 py-3.5 bg-slate-800 hover:bg-slate-900 text-white font-extrabold rounded-2xl transition-all flex items-center justify-center gap-2 shadow-md mx-auto">
          <span>閉じる</span>
        </button>
      </div>
    </div>
  </div>


  <!-- アプリのデータ＆ロジック -->
  <script>
    // --- 1. データ定義 (8系列・コース情報) ---
    const TRACKS = {
      SPACE_WEATHER: {
        id: 'SPACE_WEATHER',
        name: '宇宙・気象系列',
        color: 'from-blue-600 to-cyan-400',
        badgeColor: 'bg-cyan-100 text-cyan-800',
        mascotComment: 'データや自然の神秘、宇宙のスケールにワクワクするキミ！空や宇宙の謎を解き明かす理数アドベンチャーへ飛び出そう！',
        traits: [
          'データやグラフの変化・法則を読むのが好き',
          '天気や宇宙・自然現象への探究心がある',
          '数学的な計算や公式を使って解くのが得意'
        ],
        faculties: ['理学部', '気象大学校', '地球惑星科学科', '宇宙航空学科'],
        careers: ['気象予報士', '宇宙開発エンジニア', 'データアナリスト', '環境研究員']
      },
      DX: {
        id: 'DX',
        name: 'DX系列',
        color: 'from-purple-600 to-indigo-500',
        badgeColor: 'bg-purple-100 text-purple-800',
        mascotComment: 'デジタルテクノロジーと新アイデアの創出が得意なキミ！Web・アプリ・ゲームなど、デジタルで世界を変革しよう！',
        traits: [
          'PCやスマホの操作・活用が得意',
          '「こんなサービス欲しい！」と妄想するのが好き',
          'デジタル技術で新しい価値を作ることに興味がある'
        ],
        faculties: ['情報工学部', 'データサイエンス学部', 'デジタルコンテンツ学部'],
        careers: ['Webエンジニア', 'アプリ開発者', 'ゲームデザイナー', 'DXコンサルタント']
      },
      HYOGO_STARTUP: {
        id: 'HYOGO_STARTUP',
        name: 'ひょうごからスタートアップ系列',
        color: 'from-pink-500 to-amber-500',
        badgeColor: 'bg-pink-100 text-pink-800',
        mascotComment: '地域の魅力発信や新しい挑戦・起業に燃えるキミ！企画力と情熱で兵庫から世界へ新しい風を起こそう！',
        traits: [
          '地元の魅力を多くの人に伝えるのが好き',
          'イベントや新しい企画を立ち上げるのが好き',
          '将来自分で事業やサービスを起こす（起業）に興味がある'
        ],
        faculties: ['経営学部', '経済学部', '地域創生学部', 'アントレプレナーシップ学科'],
        careers: ['起業家', '新規事業プロデューサー', '地域活性化コーディネーター', 'イベントプロデューサー']
      },
      OUTDOOR_DISASTER: {
        id: 'OUTDOOR_DISASTER',
        name: 'スポーツ・アウトドアと防災系列',
        color: 'from-emerald-500 to-teal-600',
        badgeColor: 'bg-emerald-100 text-emerald-800',
        mascotComment: '体を動かす情熱と、災害から命を守る優しさを兼ね備えたキミ！仲間と協力して安心・安全な社会を作ろう！',
        traits: [
          '体を動かすことやアクティビティが好き',
          '防災や緊急時に人を助けることに強い興味がある',
          'チームで協力して課題に取り組み達成するのが好き'
        ],
        faculties: ['防災学部', 'スポーツ健康科学部', '社会安全学部', '救急救命学科'],
        careers: ['消防士・救急救命士', '防災コーディネーター', 'スポーツインストラクター', 'アウトドアガイド']
      },
      DIVERSITY: {
        id: 'DIVERSITY',
        name: 'ダイバーシティ&インクルージョン系列',
        color: 'from-rose-500 to-purple-500',
        badgeColor: 'bg-rose-100 text-rose-800',
        mascotComment: '多様な価値観を理解し、「誰もが過ごしやすい社会」を追求できる優しい視点を持ったキミにピッタリ！',
        traits: [
          '「当たり前」に疑問を持ち、多様な意見に耳を傾けられる',
          '自分と異なる考え方や立場の人を尊重できる',
          'いろんな人の視点から社会課題を考えられる'
        ],
        faculties: ['看護学部', '外国語学部', '総合人間科学部', '社会学部', '国際共生学部', '福祉学部'],
        careers: ['看護師・医療従事者', '語学を活かした職種', 'ダイバーシティ推進担当', '社会福祉士', '国際協力スタッフ']
      },
      LIBERAL_SCIENCE: {
        id: 'LIBERAL_SCIENCE',
        name: 'リベラルアーツ理系系列',
        color: 'from-blue-500 to-indigo-600',
        badgeColor: 'bg-blue-100 text-blue-800',
        mascotComment: '「なぜ？」をロジカルに掘り下げる探究派！特定の分野に縛られず、幅広い理系知性を身につけよう！',
        traits: [
          '理由や仕組みから本質を理解するのが好き',
          '理系進学希望だが、まだ一つの分野に絞っていない',
          '仮説を立てて試行錯誤しながら答えを探すのが好き'
        ],
        faculties: ['理学部（学科横断コース）', '総合科学部', '教養学部（理系）'],
        careers: ['サイエンスコミュニケーション', '開発研究員', 'システム分析官', '進学・大学院研究']
      },
      LIBERAL_ARTS: {
        id: 'LIBERAL_ARTS',
        name: 'リベラルアーツ文系系列',
        color: 'from-amber-600 to-rose-400',
        badgeColor: 'bg-amber-100 text-amber-800',
        mascotComment: '思考を言語化し、人間や社会の文脈を深く味わうキミ！幅広い文系知性で物事を多角的に捉えよう！',
        traits: [
          '自分の考えを文章や言葉で表現するのが好き',
          '文系進学希望だが、まだ学科を一つに絞っていない',
          '言語学・心理学・社会学など人間社会の探究が好き'
        ],
        faculties: ['文学部', '教養学部（文系）', '総合人間学科', '人文社会学科'],
        careers: ['ライター・編集者', '企画マーケター', '広報担当', '国際交流ディレクター']
      },
      CREATIVE_ARTS: {
        id: 'CREATIVE_ARTS',
        name: 'クリエイティブ・表現系列',
        color: 'from-orange-500 to-pink-500',
        badgeColor: 'bg-orange-100 text-orange-800',
        mascotComment: '自らの感性やアイデアを発信し、アートやデザインで人の心を動かすことが大好きなクリエイタータイプ！',
        traits: [
          'イラスト・音楽・映像など表現することが好き',
          '自分ならではの世界観やアイデアを持っている',
          '作品づくりを通して思いを他人に伝えたい'
        ],
        faculties: ['芸術学部', '美術学部', 'デザイン学部', '音楽学部'],
        careers: ['イラストレーター', 'グラフィックデザイナー', '映像クリエイター', '音楽制作者']
      }
    };

    // --- 2. 質問データ (全21問・4段階回答) ---
    const DIAGNOSIS_QUESTIONS = [
      // 宇宙・気象系列 (3問)
      { question: "Q1. グラフ・表などのデータから傾向や変化を読み取ることが好きだ", track: "SPACE_WEATHER", mascotEmotion: "thinking" },
      { question: "Q2. 天気・宇宙などに興味がある", track: "SPACE_WEATHER", mascotEmotion: "excited" },
      { question: "Q3. 数学の計算や公式を使って、問題を解くことに抵抗がない", track: "SPACE_WEATHER", mascotEmotion: "happy" },

      // DX系列 (3問)
      { question: "Q4. パソコン・スマートフォン操作が得意だ", track: "DX", mascotEmotion: "happy" },
      { question: "Q5. 将来Web・アプリ・ゲームに関係する職に就きたいと思う", track: "DX", mascotEmotion: "excited" },
      { question: "Q6. 「こんなサービスがあったらいいのに」など新しいものを考えるのが好きだ", track: "DX", mascotEmotion: "thinking" },

      // ひょうごからスタートアップ系列 (3問)
      { question: "Q7. 地元の魅力をみんなに知ってもらいたい！", track: "HYOGO_STARTUP", mascotEmotion: "excited" },
      { question: "Q8. イベントやサービスの企画がとても好きだ", track: "HYOGO_STARTUP", mascotEmotion: "happy" },
      { question: "Q9. 将来起業することに興味がある", track: "HYOGO_STARTUP", mascotEmotion: "talk" },

      // スポーツ・アウトドアと防災系列 (3問)
      { question: "Q10. 体を動かすことがとても好きだ", track: "OUTDOOR_DISASTER", mascotEmotion: "happy" },
      { question: "Q11. 地震や豪雨などの自然災害時に人を助けたりすることに興味がある", track: "OUTDOOR_DISASTER", mascotEmotion: "talk" },
      { question: "Q12. グループで協力して課題や活動に取り組むことが好きだ", track: "OUTDOOR_DISASTER", mascotEmotion: "excited" },

      // ダイバーシティ&インクルージョン系列 (3問)
      { question: "Q13. 当たり前のことになぜ？と疑問を持てる", track: "DIVERSITY", mascotEmotion: "thinking" },
      { question: "Q14. 自分と違う考え方の人の意見に興味がある", track: "DIVERSITY", mascotEmotion: "talk" },
      { question: "Q15. 一つの問題に様々な立場の人の意見を考えることができる", track: "DIVERSITY", mascotEmotion: "happy" },

      // リベラルアーツ理系系列 (3問)
      { question: "Q16. 「なぜそうなるか」を、理由や仕組みから理解することが好き", track: "LIBERAL_SCIENCE", mascotEmotion: "thinking" },
      { question: "Q17. 将来理系の大学に進みたいが分野が決まっていない", track: "LIBERAL_SCIENCE", mascotEmotion: "talk" },
      { question: "Q18. 仮説をたてて試行錯誤しながら答えを導くのが好きだ", track: "LIBERAL_SCIENCE", mascotEmotion: "happy" },

      // リベラルアーツ文系系列 (3問)
      { question: "Q19. 自分の考えを文章で表すことが好きだ", track: "LIBERAL_ARTS", mascotEmotion: "happy" },
      { question: "Q20. 将来文系の大学に進みたいが分野が決まっていない", track: "LIBERAL_ARTS", mascotEmotion: "talk" },
      { question: "Q21. 言語学や社会学に興味がある", track: "LIBERAL_ARTS", mascotEmotion: "excited" }
    ];

    // 大学進学が決まっている人向けのクイック選択質問
    const DECIDED_QUESTIONS = [
      {
        question: "進学したい大学の学部や学びたい分野の方向性はどれに近い？",
        track: null,
        mascotEmotion: "excited",
        isDirectBranch: true,
        options: [
          { text: "宇宙・理学・気象・データ解析系", track: "SPACE_WEATHER" },
          { text: "IT・情報・Web・ゲームアプリ系", track: "DX" },
          { text: "経営・経済・地域創生・ビジネス企画系", track: "HYOGO_STARTUP" },
          { text: "スポーツ・健康・防災・社会安全系", track: "OUTDOOR_DISASTER" },
          { text: "社会学・国際共生・福祉・人権系", track: "DIVERSITY" },
          { text: "理系全般（まだ具体的な学科を絞りたくない）", track: "LIBERAL_SCIENCE" },
          { text: "文系全般（まだ具体的な学科を絞りたくない）", track: "LIBERAL_ARTS" }
        ]
      }
    ];

    // --- 3. 4段階選択肢の定義 ---
    const FOUR_CHOICES = [
      { text: "とても当てはまる", score: 4, style: "hover:bg-purple-600 hover:text-white border-purple-300" },
      { text: "やや当てはまる", score: 3, style: "hover:bg-purple-500 hover:text-white border-purple-200" },
      { text: "あまり当てはまらない", score: 2, style: "hover:bg-slate-400 hover:text-white border-slate-200" },
      { text: "全く当てはまらない", score: 1, style: "hover:bg-slate-500 hover:text-white border-slate-200" }
    ];

    // --- 4. 画像URLの設定プレースホルダー ---
    // 自作キャラクター画像がある場合、以下のURLを書き換えてください。
    // 例: MASCOT_IMAGES.happy = "https://your-domain.com/path/to/character_happy.png";
    const MASCOT_IMAGES = {
      happy: null,     // nullの場合はデフォルトのSVGキャラを表示
      thinking: null,
      excited: null,
      talk: null
    };

    // --- 5. アプリの状態管理 ---
    let state = {
      isDecidedPath: false,
      currentQuestionIndex: 0,
      activeQuestions: [],
      scores: {
        SPACE_WEATHER: 0,
        DX: 0,
        HYOGO_STARTUP: 0,
        OUTDOOR_DISASTER: 0,
        DIVERSITY: 0,
        LIBERAL_SCIENCE: 0,
        LIBERAL_ARTS: 0
      }
    };

    // --- 6. キャラクター表示処理 (画像URLまたはSVG) ---
    function getMascotHTML(emotion = 'happy') {
      const customImgUrl = MASCOT_IMAGES[emotion] || MASCOT_IMAGES['happy'];
      if (customImgUrl) {
        return `<img src="${customImgUrl}" alt="ナビィ" class="w-full h-full object-contain animate-float" />`;
      }

      // SVGフォールバック
      let eyeSVG = `<circle cx="38" cy="48" r="4" fill="#0F172A"/><circle cx="62" cy="48" r="4" fill="#0F172A"/>`;
      let mouthSVG = `<path d="M 43 56 Q 50 63 57 56" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none"/>`;

      if (emotion === 'thinking') {
        eyeSVG = `<path d="M 34 46 Q 38 43 42 46" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round"/><circle cx="62" cy="48" r="4" fill="#0F172A"/>`;
        mouthSVG = `<path d="M 45 58 Q 50 56 55 58" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none"/>`;
      } else if (emotion === 'excited') {
        eyeSVG = `<path d="M 33 48 L 41 44 L 33 40" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none"/>
                  <path d="M 67 48 L 59 44 L 67 40" stroke="#0F172A" stroke-width="2.5" stroke-linecap="round" fill="none"/>`;
        mouthSVG = `<ellipse cx="50" cy="58" rx="6" ry="5" fill="#0F172A"/>`;
      } else if (emotion === 'talk') {
        mouthSVG = `<ellipse cx="50" cy="57" rx="4" ry="3" fill="#0F172A"/>`;
      }

      return `
        <svg viewBox="0 0 100 100" class="w-full h-full drop-shadow">
          <circle cx="50" cy="50" r="42" fill="#F3E8FF"/>
          <path d="M 25 45 C 25 20, 75 20, 75 45 Z" fill="#8B5CF6"/>
          <circle cx="28" cy="40" r="8" fill="#8B5CF6"/>
          <circle cx="72" cy="40" r="8" fill="#8B5CF6"/>
          ${eyeSVG}
          <ellipse cx="33" cy="53" rx="4" ry="2.5" fill="#FF6B9B" opacity="0.6"/>
          <ellipse cx="67" cy="53" rx="4" ry="2.5" fill="#FF6B9B" opacity="0.6"/>
          ${mouthSVG}
        </svg>
      `;
    }

    // --- 7. 画面制御 & ロジック ---
    function showScreen(screenId) {
      ['screen-start', 'screen-branch', 'screen-quiz', 'screen-result'].forEach(id => {
        document.getElementById(id).classList.add('hidden');
      });
      document.getElementById(screenId).classList.remove('hidden');
    }

    function animateText(elementId, text, speed = 25) {
      // 文字がカタカタ表示される演出を廃止し、即時表示にする
      const el = document.getElementById(elementId);
      el.textContent = text;
    }

    function startApp() {
      showScreen('screen-branch');
      animateText('branch-text', '教えて！進学したい大学や学びたい分野は、もう具体的に決まっているかな？');
    }

    function selectBranch(isDecided) {
      state.isDecidedPath = isDecided;
      state.currentQuestionIndex = 0;
      Object.keys(state.scores).forEach(k => state.scores[k] = 0);

      state.activeQuestions = isDecided ? DECIDED_QUESTIONS : DIAGNOSIS_QUESTIONS;
      showScreen('screen-quiz');
      renderQuestion();
    }

    function renderQuestion() {
      const q = state.activeQuestions[state.currentQuestionIndex];
      const total = state.activeQuestions.length;
      const currentNum = state.currentQuestionIndex + 1;
      const progressPercent = Math.round((currentNum / total) * 100);

      document.getElementById('quiz-progress-text').textContent = `QUESTION ${currentNum} / ${total}`;
      document.getElementById('quiz-progress-percent').textContent = `${progressPercent}%`;
      document.getElementById('quiz-progress-bar').style.width = `${progressPercent}%`;

      document.getElementById('quiz-mascot-avatar').innerHTML = getMascotHTML(q.mascotEmotion);
      animateText('quiz-question-text', q.question, 20);

      const optionsContainer = document.getElementById('quiz-options-container');
      optionsContainer.innerHTML = '';

      // 大学決定ルートのダイレクト選択肢の場合
      if (q.isDirectBranch) {
        q.options.forEach((opt) => {
          const btn = document.createElement('button');
          btn.className = "w-full glass-card p-4 rounded-2xl hover:bg-purple-600 hover:text-white transition-all text-left font-bold text-slate-700 border-2 border-white shadow-sm flex items-center justify-between group";
          btn.innerHTML = `
            <span class="text-xs sm:text-sm">${opt.text}</span>
            <i class="fa-solid fa-chevron-right text-slate-300 group-hover:text-white transition-colors"></i>
          `;
          btn.onclick = () => {
            state.scores[opt.track] = 12; // 一括最大スコア付与
            showResults();
          };
          optionsContainer.appendChild(btn);
        });
        return;
      }

      // 通常診断ルートの4段階評価選択肢
      FOUR_CHOICES.forEach((choice) => {
        const btn = document.createElement('button');
        btn.className = `w-full glass-card p-4 rounded-2xl transition-all text-left font-bold text-slate-700 border-2 shadow-sm flex items-center justify-between group active:scale-[0.98] ${choice.style}`;
        btn.innerHTML = `
          <span class="text-xs sm:text-sm">${choice.text}</span>
          <span class="text-xs font-black opacity-60 group-hover:opacity-100">+${choice.score}pt</span>
        `;
        btn.onclick = () => answerQuestion(q.track, choice.score);
        optionsContainer.appendChild(btn);
      });
    }

    function answerQuestion(trackKey, score) {
      state.scores[trackKey] += score;
      state.currentQuestionIndex++;

      if (state.currentQuestionIndex < state.activeQuestions.length) {
        renderQuestion();
      } else {
        showResults();
      }
    }

    function showResults() {
      // 全系列のスコア計算
      let maxScore = -1;
      let topTrackKey = 'SPACE_WEATHER';

      Object.keys(state.scores).forEach(key => {
        if (state.scores[key] > maxScore) {
          maxScore = state.scores[key];
          topTrackKey = key;
        }
      });

      const result = TRACKS[topTrackKey];
      document.getElementById('result-title').textContent = result.name;
      document.getElementById('result-mascot-comment').textContent = result.mascotComment;

      // 最高12点（3問×4点）をベースにした適合度算出
      const maxPossibleScore = 12;
      const matchScore = state.isDecidedPath ? 99 : Math.min(99, Math.round((maxScore / maxPossibleScore) * 100));
      document.getElementById('result-match-score').textContent = `${matchScore}%`;

      showScreen('screen-result');

      setTimeout(() => {
        document.getElementById('result-match-bar').style.width = `${matchScore}%`;
      }, 100);

      // 特徴リスト
      document.getElementById('result-traits').innerHTML = result.traits.map(t => `
        <li class="flex items-start gap-2">
          <i class="fa-solid fa-check text-purple-600 mt-1"></i>
          <span>${t}</span>
        </li>
      `).join('');

      // 学部バッジ
      document.getElementById('result-faculties').innerHTML = result.faculties.map(f => `
        <span class="px-2.5 py-1 rounded-lg ${result.badgeColor} font-bold text-xs">${f}</span>
      `).join('');

      // 職種バッジ
      document.getElementById('result-careers').innerHTML = result.careers.map(c => `
        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 font-bold text-xs border border-slate-200">${c}</span>
      `).join('');

      renderModalTracksList();
    }

    function restartApp() {
      document.getElementById('result-match-bar').style.width = '0%';
      showScreen('screen-start');
    }

    // --- SNSサイドバー制御 ---
    function toggleSnsSidebar() {
      const sidebar = document.getElementById('sidebar-sns');
      sidebar.classList.toggle('translate-x-full');
    }

    // --- KIKS学校説明モーダル ---
    function openSchoolModal() {
      document.getElementById('modal-school-info').classList.remove('hidden');
    }
    function closeSchoolModal() {
      document.getElementById('modal-school-info').classList.add('hidden');
    }

    // --- 系列説明モーダル制御 ---
    function openTracksListModal() {
      renderTrackButtons();
      // デフォルトで最初の系列を選択
      selectTrackDetail(Object.keys(TRACKS)[0]);
      document.getElementById('modal-tracks-selector').classList.remove('hidden');
    }

    function closeTracksListModal() {
      document.getElementById('modal-tracks-selector').classList.add('hidden');
    }

    function renderTrackButtons() {
      const grid = document.getElementById('tracks-button-grid');
      grid.innerHTML = Object.values(TRACKS).map(t => `
        <button onclick="selectTrackDetail('${t.id}')" id="btn-track-${t.id}" class="track-select-btn p-2 rounded-xl border text-center font-bold text-xs transition-all hover:border-purple-400 bg-white/80 text-slate-700">
          ${t.name.replace('系列', '')}
        </button>
      `).join('');
    }

    function selectTrackDetail(trackId) {
      const t = TRACKS[trackId];
      if (!t) return;

      // ボタンのアクティブ状態更新
      document.querySelectorAll('.track-select-btn').forEach(btn => {
        btn.classList.remove('bg-purple-600', 'text-white', 'border-purple-600');
        btn.classList.add('bg-white/80', 'text-slate-700');
      });
      const activeBtn = document.getElementById(`btn-track-${trackId}`);
      if (activeBtn) {
        activeBtn.classList.remove('bg-white/80', 'text-slate-700');
        activeBtn.classList.add('bg-purple-600', 'text-white', 'border-purple-600');
      }

      // 詳細の表示
      const display = document.getElementById('track-detail-display');
      display.innerHTML = `
        <div class="space-y-3">
          <div class="flex items-center justify-between">
            <h4 class="font-black text-slate-800 text-base">${t.name}</h4>
            <span class="text-xs font-bold px-2.5 py-1 rounded-full ${t.badgeColor}">詳細</span>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed bg-white/80 p-3 rounded-xl border border-slate-100">${t.mascotComment}</p>

          <div>
            <span class="font-extrabold text-xs text-slate-500 block mb-1">【主な特徴】</span>
            <ul class="space-y-1">
              ${t.traits.map(trait => `<li class="text-xs text-slate-700 flex items-center gap-1.5"><i class="fa-solid fa-check text-purple-500 text-[10px]"></i> ${trait}</li>`).join('')}
            </ul>
          </div>

          <div class="grid grid-cols-2 gap-2 pt-1">
            <div>
              <span class="font-extrabold text-[11px] text-slate-500 block mb-1">【目指せる学部】</span>
              <div class="flex flex-wrap gap-1">
                ${t.faculties.map(f => `<span class="text-[10px] px-2 py-0.5 rounded bg-slate-100 font-bold text-slate-700">${f}</span>`).join('')}
              </div>
            </div>
            <div>
              <span class="font-extrabold text-[11px] text-slate-500 block mb-1">【主な適性職種】</span>
              <div class="flex flex-wrap gap-1">
                ${t.careers.map(c => `<span class="text-[10px] px-2 py-0.5 rounded bg-purple-50 font-bold text-purple-700">${c}</span>`).join('')}
              </div>
            </div>
          </div>
        </div>
      `;
    }

    function shareResult() {
      const title = document.getElementById('result-title').textContent;
      const shareText = `【未来ルートナビ】私の適性診断結果は「${title}」でした！✨ #高校コース診断 #未来ルートナビ`;
      
      // Fallback implementation using document.execCommand('copy') for iframe compatibility
      try {
        const tempInput = document.createElement('textarea');
        tempInput.value = shareText;
        tempInput.style.position = 'fixed';
        tempInput.style.opacity = '0';
        document.body.appendChild(tempInput);
        tempInput.select();
        const successful = document.execCommand('copy');
        document.body.removeChild(tempInput);

        if (successful) {
          showShareNotification('診断結果をクリップボードにコピーしました！✨');
        } else {
          showShareNotification(shareText);
        }
      } catch (err) {
        showShareNotification(shareText);
      }
    }

    function showShareNotification(msg) {
      // Create a temporary subtle toast message instead of alert()
      const toast = document.createElement('div');
      toast.className = 'fixed bottom-6 left-1/2 -translate-x-1/2 bg-slate-900/90 text-white text-xs font-bold px-4 py-3 rounded-2xl shadow-xl z-50 transition-all transform duration-300 max-w-sm text-center border border-slate-700';
      toast.textContent = msg;
      document.body.appendChild(toast);
      
      setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
      }, 3000);
    }

    function renderModalTracksList() {
      const container = document.getElementById('modal-tracks-list');
      container.innerHTML = Object.values(TRACKS).map(t => `
        <div class="p-4 rounded-2xl bg-white/90 border border-purple-100 shadow-sm">
          <div class="flex items-center justify-between mb-1.5">
            <span class="font-extrabold text-sm text-slate-800">${t.name}</span>
            <span class="text-[10px] px-2 py-0.5 rounded-full ${t.badgeColor} font-bold">適性コース</span>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">${t.traits.join(' / ')}</p>
        </div>
      `).join('');
    }

    function toggleAllTracksModal() {
      document.getElementById('modal-all-tracks').classList.toggle('hidden');
    }
  </script>
</body>
</html>