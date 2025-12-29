from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# --- Datos de los vértices para el PATO RONAL ---
# Hemos movido todos los puntos a esta estructura de datos.
# Cada elemento es una tupla que contiene:
# 1. El modo de dibujo (ej. GL_LINE_LOOP, GL_LINE_STRIP)
# 2. Una lista de tuplas (x, y) con los vértices.
pato_parts = [
    # Pie derecho
    (GL_LINE_LOOP, [(-5, -9), (-4, -10), (-5, -11), (-5, -13), (4, -13), (-1, -11), (-2, -10), (-3, -8)]),
    # Pie izquierdo
    (GL_LINE_STRIP, [(-9, -7), (-10, -9), (-10, -10), (-9, -11), (-10, -12), (-12, -13), (-13, -14), (-6, -14), (-5, -14), (-5, -13), (-5, -12), (-8, -9), (-7, -8)]),
    # Contorno principal del cuerpo (lado izquierdo y barriga)
    (GL_LINE_STRIP, [(-10, -9), (-10, -8), (-11, -7), (-12, -5), (-12, -4), (-11, -2), (-8, -1), (-7, -3), (-5, -5), (-3, -6), (-1, -6), (-2, -7), (-3, -8), (-5, -9), (-8, -9)]),
    
    # --- PICO ---
    # Parte superior externa del pico
    (GL_LINE_STRIP, [(-8, -1), (-7, 0), (-6, 2), (-3, 3), (-1, 1), (0, 1), (1, -1)]), 
    # Línea de la parte superior del pico hacia el ojo
    (GL_LINE_STRIP, [(-1, 3), (0, 1)]), 
    # Parte inferior externa del pico
    (GL_LINE_STRIP, [(-7, 0), (-5, -1), (-5, -2), (-4, -2), (-1, -3), (0, -1), (1, -1)]), 
    # Línea de la parte inferior del pico hacia el cuerpo
    (GL_LINE_STRIP, [(-1, -2), (-3, 0), (-4, 1)]), 
    # Boca, mandíbula inferior y mano derecha
    (GL_LINE_LOOP, [(0, -1), (-1, -2), (-1, -3), (1, -5), (2, -7), (3, -6), (2, -4), (3, -5), (3, -6), (4, -6), (4, -5), (5, -5), (5, -4), (4, -2)]), 
    # --- FIN DEL PICO ---

    # Contorno de la cabeza y gorro
    (GL_LINE_STRIP, [(-3, 3), (-6, 3), (-9, 6), (-9, 8), (-8, 10), (-6, 12), (-2, 12), (0, 13), (1, 14), (3, 14), (5, 12), (2, 9), (0, 9), (1, 8), (3, 9), (4, 8), (4, 7), (3, 6), (2, 6), (3, 4), (1, 3), (-1, 4), (-1, 3)]),
    # Detalle interno del gorro (lado izquierdo)
    (GL_LINE_STRIP, [(-9, 6), (-8, 8), (-5, 11), (-2, 12)]),
    # Ojo izquierdo
    (GL_LINE_LOOP, [(-2, 9), (-4, 8), (-5, 9), (-4, 11), (-3, 11)]),
    # Pupila izquierda
    (GL_LINE_LOOP, [(-3, 10), (-4, 10), (-4, 9)]),
    # Ojo derecho
    (GL_LINE_LOOP, [(0, 9), (-1, 10), (0, 11), (1, 10)]),
    # Pupila derecha
    (GL_LINE_STRIP, [(-1, 10), (0, 10), (0, 9)]),
    # Cuello de la camisa
    (GL_LINE_LOOP, [(3, 6), (-2, 6), (-3, 7), (-3, 6), (1, 4), (2, 4), (1, 6)]),
    # Cuadrado/Pompón del gorro
    (GL_LINE_LOOP, [(-8, 10), (-8, 11), (-9, 11), (-9, 10)]),
    # Detalle interno del gorro (cerca del ojo)
    (GL_LINE_LOOP, [(-8, 8), (-8, 10), (-5, 11)]),
    # Línea del pompón
    (GL_LINE_STRIP, [(-8, 10), (-8, 11)]),
    # Detalle interno del gorro (superior)
    (GL_LINE_STRIP, [(-2, 12), (0, 11)]),
    # Detalle del brazo/cuerpo (línea interna)
    (GL_LINE_STRIP, [(-1, -6), (0, -4)]),
    # Detalle de la mano derecha (dedos)
    (GL_LINE_LOOP, [(4, -5), (4, -4), (3, -3)]),
    # Cola (contorno)
    (GL_LINE_LOOP, [(-12, -4), (-12, 0), (-14, -1), (-13, -1)]),
    # Cola (detalle interno)
    (GL_LINE_STRIP, [(-12, -4), (-13, -2), (-14, -5), (-13, -4), (-10, -5)]),
    # Hombro/Brazo izquierdo
    (GL_LINE_LOOP, [(-8, -1), (-8, 1), (-6, 2)]),
]

def inicializar():
    """Función de inicialización de OpenGL."""
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glPointSize(2)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-15.0, 15.0, -15.0, 15.0, -15.0, 15.0)

def dibujar_PATO_RONAL():
    """Dibuja el pato iterando sobre la lista de partes."""
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Iteramos sobre cada parte (modo y vértices) definida en la lista
    for mode, vertices in pato_parts:
        glBegin(mode)
        # Iteramos sobre cada vértice (x, y) en la lista de vértices
        for x, y in vertices:
            glVertex2f(x, y)
        glEnd()

    glFlush()

def main():
    """Función principal para configurar GLUT y correr el bucle."""
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"PATO de puntos en OpenGL (Comentado)")
    
    inicializar()
    
    glutDisplayFunc(dibujar_PATO_RONAL)
    glutMainLoop()

if __name__ == "__main__":
    main()

