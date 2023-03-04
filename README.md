# Mystudy

## chatbot
### 概要・構成
* 居酒屋を予約するチャットボット
　※ChatbotそのものはGoogleDialogFlow上で作成。
　WebhookをCloudFonction上に配置し、細かな制御を実装。
  予約表はBigQueryのテーブルを席予約表と見なしてデータを投げている。
  
  - 
  -
  -
 

## SemanticSegmentation
### 概要・構成
* Local環境上でMask-RNCC-TF2（https://github.com/ahmedfgad/Mask-RCNN-TF2）を実行
  トライアルとして犬の種類を5種類に絞り、SemanticSegmentationで識別できるかに取り組む。
  教師データはLocalDockerコンテナ上でLabelStudio（https://labelstud.io/）を立ち上げ、アノテーションを実施。
  
  - DogSegment_predict.py（予定）
  - DogSegment_train.py(予定）
  
  
