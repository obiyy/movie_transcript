# YouTube字幕取得API

YouTubeの動画URLをPOSTすると、英語字幕を取得して仮の日本語訳とともに返す簡単なFlaskアプリです。

## エンドポイント
POST /get_subtitles  
Body:
```json
{
  "url": "https://www.youtube.com/watch?v=XXXXXXX"
}
