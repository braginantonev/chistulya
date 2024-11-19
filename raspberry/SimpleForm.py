import cv2
import numpy as np


def preprocess_image(image):
    # Преобразуем изображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применяем гауссово размытие для уменьшения шума
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    return blurred


def detect_boundaries(image):
    # Предобработка изображения
    preprocessed = preprocess_image(image)

    # Применяем оператор Canny для выделения границ
    edges = cv2.Canny(preprocessed, 50, 150)

    return edges


def draw_boundaries(image, edges):
    # Копируем изображение, чтобы не изменять оригинал
    result_image = image.copy()

    # Находим контуры на изображении с границами
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Рисуем контуры красным цветом
    for contour in contours:
        cv2.drawContours(result_image, [contour], -1, (0, 0, 255), 2)

    return result_image


# Пример использования
if __name__ == "__main__":
    # Захват видео с камеры
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Определяем границы
        edges = detect_boundaries(frame)

        # Рисуем границы на изображении
        result_image = draw_boundaries(frame, edges)

        # Отображаем результат
        cv2.imshow('Boundary Detection', result_image)

        # Выход по нажатию клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
