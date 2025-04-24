async def handleEmotionMessage(conn, emotion_data):
    """处理情绪消息"""
    conn.current_emotion = emotion_data["emotion"]
    conn.emotion_confidence = int(emotion_data["confidence"])
    conn.last_emotion_update = time.time()
    logger.bind(tag=TAG).info(f"更新情绪状态: {conn.current_emotion}, 置信度: {conn.emotion_confidence}%")