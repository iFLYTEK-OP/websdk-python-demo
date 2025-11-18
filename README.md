# 一、PYTHON-SDK-DEMO信息获取与运行



## 1、能力使用的 APPID、APISecret、APIKey获取



请点击[控制台](https://console.xfyun.cn/services)进行获取并填写到 .env 文件！



## 4、DEMO运行说明



获取到信息后填写到项目路径 .env 文件中，找到能力对应的主类运行即可。能力与主类对应说明如下：

| AI能力名称                                                   | 对应主类名称                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 语音听写                                                     | [iat_test.py](xfyunsdkdemo/speech/iat_test.py)               |
| 实时语音转写                                                 | [rtasr_test.py](xfyunsdkdemo/speech/rtasr_test.py)           |
| 音频文件语音转写                                             | [lfasr_test.py](xfyunsdkdemo/speech/lfasr_test.py)           |
| 语音合成                                                     | [tts_test.py](xfyunsdkdemo/speech/tts_test.py)               |
| 语音评测                                                     | [ise_test.py](xfyunsdkdemo/speech/ise_test.py)               |
| 小牛翻译及自研机器翻译                                       | [translate_test.py](xfyunsdkdemo/nlp/translate_test.py)      |
| 文本纠错                                                     | [text_check_test.py](xfyunsdkdemo/nlp/text_check_test.py)    |
| 智能PPT（新）                                                | [ai_ppt_test.py](xfyunsdkdemo/spark/ai_ppt_test.py)          |
| 静默活体检测                                                 | [anti_spoof_test.py](xfyunsdkdemo/face/anti_spoof_test.py)   |
| 银行卡识别                                                   | [bank_card_test.py](xfyunsdkdemo/ocr/bank_card_test.py)      |
| 名片识别                                                     | [business_card_test.py](xfyunsdkdemo/ocr/business_card_test.py) |
| 人脸比对                                                     | [face_compare_test.py](xfyunsdkdemo/face/face_compare_test.py) |
| 人脸检测和属性分析                                           | [face_detect_test.py](xfyunsdkdemo/face/face_detect_test.py) |
| 配合式活体检测                                               | [face_status_test.py](xfyunsdkdemo/face/face_status_test.py) |
| 人脸比对sensetime                                            | [face_verify_test.py](xfyunsdkdemo/face/face_verify_test.py) |
| 指尖文字识别                                                 | [finger_ocr_test.py](xfyunsdkdemo/ocr/finger_ocr_test.py)    |
| 印刷文字识别和手写文字识别                                   | [general_words_test.py](xfyunsdkdemo/ocr/general_words_test.py) |
| 性别年龄识别                                                 | [igr_test.py](xfyunsdkdemo/speech/igr_test.py)               |
| 场景识别和物体识别和场所识别                                 | [rec_ocr_test.py](xfyunsdkdemo/ocr/rec_ocr_test.py)          |
| 图片类识别（营业执照,出租车发票,火车票,增值税发票 ,身份证,印刷文字） | [image_word_test.py](xfyunsdkdemo/ocr/image_word_test.py)    |
| 身份证识别 营业执照识别 增值税发票识别 印刷文字识别（多语种） | [intsig_ocr_test.py](xfyunsdkdemo/ocr/intsig_ocr_test.py)    |
| 歌曲识别                                                     | [qbh_test.py](xfyunsdkdemo/speech/qbh_test.py)               |
| 静默活体检测sensetime                                        | [silent_detect_test.py](xfyunsdkdemo/face/silent_detect_test.py) |
| 人脸检测和属性分析                                           | [tup_api_test.py](xfyunsdkdemo/face/tup_api_test.py)         |
| 人脸水印照比对                                               | [watermark_verify_test.py](xfyunsdkdemo/face/watermark_verify_test.py) |
| 超拟人合成                                                   | [oral_test.py](xfyunsdkdemo/spark/oral_test.py)              |
| 简历生成                                                     | [resume_generate_test.py](xfyunsdkdemo/spark/resume_generate_test.py) |
| 多语种大模型语音听写、方言大模型语音听写、中文大模型语音听写 | [spark_iat_test.py](xfyunsdkdemo/spark/spark_iat_test.py)    |
| 一句话复刻                                                   | [voice_clone_test.py](xfyunsdkdemo/spark/voice_clone_test.py) |
| 一句话训练                                                   | [train_test.py](xfyunsdkdemo/spark/train_test.py)            |
| 音频合规                                                     | [audio_moderation_test.py](xfyunsdkdemo/nlp/audio_moderation_test.py) |
| 图片合规                                                     | [image_moderation_test.py](xfyunsdkdemo/nlp/image_moderation_test.py) |
| 同声传译                                                     | [sim_interp_test.py](xfyunsdkdemo/nlp/sim_interp_test.py)    |
| 文本合规                                                     | [text_moderation_test.py](xfyunsdkdemo/nlp/text_moderation_test.py) |
| 文本校对                                                     | [text_proof_test.py](xfyunsdkdemo/nlp/text_proof_test.py)    |
| 文本改写                                                     | [text_rewrite_test.py](xfyunsdkdemo/nlp/text_rewrite_test.py) |
| 视频合规                                                     | [video_moderation_test.py](xfyunsdkdemo/nlp/video_moderation_test.py) |
| 词库操作                                                     | [wordlib_test.py](xfyunsdkdemo/nlp/wordlib_test.py)          |
| 星火智能体                                                   | [agent_test.py](xfyunsdkdemo/spark/agent_test.py)            |
| 超拟人交互                                                   | [oral_chat_test.py](xfyunsdkdemo/spark/oral_chat_test.py)    |
| 通用大模型识别                                               | [llm_ocr_test.py](xfyunsdkdemo/ocr/llm_ocr_test.py)          |
| 超拟人个性化知识库                                           | [aiui_knowledge_test.py](xfyunsdkdemo\spark\aiui_knowledge_test.py) |

# 二、讯飞开放平台常用AI能力介绍与常用参数说明



## 1、语音听写（流式版）



### （1）功能说明



语音听写流式接口，用于1分钟内的即时语音转文字技术，支持实时返回识别结果，达到一边上传音频一边获得识别文本的效果。

### （2）常用参数



以下仅为常用参数说明，详情请点击[语音听写文档](https://www.xfyun.cn/doc/asr/voicedictation/API.html#接口说明) 查看。

| 参数名  | 类型   | 必传 | 描述                                                         | 示例   |
| ------- | ------ | ---- | ------------------------------------------------------------ | ------ |
| vad_eos | int    | 否   | 用于设置端点检测的静默时间，单位是毫秒。 即静默多长时间后引擎认为音频结束。 默认2000（小语种除外，小语种不设置该参数默认为未开启VAD）。 | 3000   |
| dwa     | string | 否   | （仅中文普通话支持）动态修正 wpgs：开启流式结果返回功能 *注：该扩展功能若未授权无法使用，可到控制台-语音听写（流式版）-高级功能处免费开通；若未授权状态下设置该参数并不会报错，但不会生效。* | "wpgs" |

## 2、实时语音转写



### （1）功能说明



实时语音转写（Real-time ASR）基于深度全序列卷积神经网络框架，通过 WebSocket 协议，建立应用与语言转写核心引擎的长连接，开发者可实现将连续的音频流内容，实时识别返回对应的文字流内容。 支持的音频格式： 采样率为16K，采样深度为16bit的pcm_s16le音频

### （2）常用参数



以下仅为常用参数说明，详情请点击[实时语音转写文档](https://www.xfyun.cn/doc/asr/rtasr/API.html)查看。

| 参数名                                                       | 类型   | 必传 | 描述                             | 示例                                                         |
| ------------------------------------------------------------ | ------ | ---- | -------------------------------- | ------------------------------------------------------------ |
| lang                                                         | string | 否   | 实时语音转写语种，不传默认为中文 |                                                              |
| 语种类型：中文、中英混合识别：cn；英文：en；小语种及方言可到控制台-实时语音转写-方言/语种处添加，添加后会显示该方言/语种参数值。传参示例如：" |        |      |                                  |                                                              |
| lang=en"                                                     |        |      |                                  |                                                              |
| targetLang                                                   | string | 否   | 目标翻译语种                     | 例如：targetLang="en" 如果使用中文实时翻译为英文传参示例如下： " |
| &lang=cn&transType=normal&transStrategy=2&targetLang=en" 注意：需控制台开通翻译功能 |        |      |                                  |                                                              |

## 3、音频文件语音转写



### （1）功能说明



语音转写（Long Form ASR）基于深度全序列卷积神经网络，将长段音频（5小时以内）数据转换成文本数据，为信息处理和数据挖掘提供基础。 转写的是已录制音频（非实时），音频文件上传成功后进入等待队列，待转写成功后用户即可获取结果，返回结果时间受音频时长以及排队任务量的影响。 如遇转写耗时比平时延长，大概率表示当前时间段出现转写高峰，请耐心等待即可，我们承诺有效任务耗时最大不超过5小时 。 另外，为使转写服务更加通畅，请尽量转写5分钟以上的音频文件。

### （2）常用参数



以下仅为常用参数说明，详情请点击[音频文件语音转写文档](https://www.xfyun.cn/doc/asr/ifasr_new/API.html)查看。

| 参数名                                                       | 类型                                  | 必传 | 描述                                                  | 示例                     |
| ------------------------------------------------------------ | ------------------------------------- | ---- | ----------------------------------------------------- | ------------------------ |
| speaker_number                                               | string                                | 否   | 发音人个数，可选值：0-10，0表示盲分 *注*              |                          |
| ：发音人分离目前还是测试效果达不到商用标准，如测试无法满足您的需求，请慎用该功能。 | 默认：2（适用通话时两个人对话的场景） |      |                                                       |                          |
| has_seperate                                                 | string                                | 否   | 转写结果中是否包含发音人分离信息                      | false或true，默认为false |
| role_type                                                    | string                                | 否   | 支持两种参数 1: 通用角色分离 2:                       |                          |
| 电话信道角色分离（适用于speaker_number为2的说话场景）该字段只有在开通了角色分离功能的前提下才会生效，正确传入该参数后角色分离效果会有所提升。 |                                       |      |                                                       |                          |
| 如果该字段不传，默认采用 1 类型                              |                                       |      |                                                       |                          |
| language                                                     | string                                | 否   | 语种 cn:中英文&中文（默认） en:英文（英文不支持热词） | cn                       |

## 4、语音合成（流式版）



### （1）功能说明



语音合成流式接口将文字信息转化为声音信息，同时提供了众多极具特色的发音人（音库）供您选择，可以在 这里 在线体验发音人效果。

### （2）常用参数



以下仅为常用参数说明，详情请点击[语音合成文档](https://www.xfyun.cn/doc/tts/online_tts/API.html)查看。

| 参数名 | 类型   | 必传 | 描述                                                         | 示例      |
| ------ | ------ | ---- | ------------------------------------------------------------ | --------- |
| vcn    | string | 是   | 发音人，可选值：请到控制台添加试用或购买发音人，添加后即显示发音人参数值 | "xiaoyan" |
| rdn    | string | 否   | 合成音频数字发音方式 0：自动判断（默认值） 1：完全数值 2：完全字符串 3：字符串优先 | "0"       |

## 5、语音评测（流式版）



### （1）功能说明



通过智能语音技术自动对发音水平进行评价、发音错误、缺陷定位和问题分析的能力接口。涉及的核心技术主要可分为两个部分：中文普通话发音水平自动评测技术、英文发音水平自动评测技术。

### （2）常用参数



以下仅为常用参数说明，详情请点击[语音评测文档](https://www.xfyun.cn/doc/Ise/IseAPI.html)查看。

| 参数名        | 类型   | 必传 | 描述                                                         | 示例                    |
| ------------- | ------ | ---- | ------------------------------------------------------------ | ----------------------- |
| ent           | string | 是   | 中文：cn_vip 英文：en_vip                                    | "cn_vip"                |
| category      | string | 是   | 中文题型： read_syllable（单字朗读，汉语专有） read_word（词语朗读） read_sentence（句子朗读） read_chapter(篇章朗读) 英文题型： read_word（词语朗读） read_sentence（句子朗读） read_chapter(篇章朗读) simple_expression（英文情景反应） read_choice（英文选择题） topic（英文自由题） retell（英文复述题） picture_talk（英文看图说话） oral_translation（英文口头翻译） | "read_sentence"         |
| text          | string | 是   | 待评测文本 utf8 编码，需要加utf8bom 头                       | '\uFEFF'+text           |
| tte           | string | 是   | 待评测文本编码 utf-8 gbk                                     | "utf-8"                 |
| extra_ability | string | 否   | 拓展能力（生效条件ise_unite="1", rst="entirety"）多维度分信息显示（准确度分、流畅度分、完整度打分）extra_ability值为multi_dimension（字词句篇均适用,如选多个能力，用分号；隔开。例如：add("extra_ability"," syll_phone_err_msg;pitch;multi_dimension")）单词基频信息显示（基频开始值、结束值）extra_ability值为pitch ，仅适用于单词和句子题型音素错误信息显示（声韵、调型是否正确）extra_ability值为syll_phone_err_msg（字词句篇均适用,如选多个能力，用分号；隔开。例如：add("extra_ability"," syll_phone_err_msg;pitch;multi_dimension")） | "multi_dimension"       |
| aue           | string | 否   | 音频格式 raw: 未压缩的pcm格式音频或wav（如果用wav格式音频，建议去掉头部） lame: mp3格式音频 speex-wb;7: 讯飞定制speex格式音频(默认值) | "raw"                   |
| auf           | string | 否   | 音频采样率 默认 audio/L16;rate=16000                         | "audio L16；rate=16000" |
| group         | string | 否   | 针对群体不同，相同试卷音频评分结果不同 （仅中文字、词、句、篇章题型支持），此参数会影响准确度得分 adult（成人群体，不设置群体参数时默认为成人） youth（中学群体 pupil（小学群体，中文句、篇题型设置此参数值会有accuracy_score得分的返回）） | "adult"                 |
| grade         | string | 否   | 设置评测的学段参数 （仅中文题型：中小学的句子、篇章题型支持） junior(1,2年级) middle(3,4年级) senior(5,6年级) | "middle"                |
| rst           | string | 否   | 评测返回结果与分制控制（评测返回结果与分制控制也会受到ise_unite与plev参数的影响） 完整：entirety（默认值） 中文百分制推荐传参（rst="entirety"且ise_unite="1"且配合extra_ability参数使用） 英文百分制推荐传参（rst="entirety"且ise_unite="1"且配合extra_ability参数使用） 精简：plain（评测返回结果将只有总分），如： <total_score value="98.507320"/> | "entirety"              |
| ise_unite     | string | 否   | 返回结果控制 0：不控制（默认值） 1：控制（extra_ability参数将影响全维度等信息的返回） | "0"                     |
| plev          | string | 否   | 在rst="entirety"（默认值）且ise_unite="0"（默认值）的情况下plev的取值不同对返回结果有影响。 plev：0(给出全部信息，汉语包含rec_node_type、perr_msg、fluency_score、phone_score信息的返回；英文包含accuracy_score、serr_msg、 syll_accent、fluency_score、standard_score、pitch信息的返回) | "0"                     |