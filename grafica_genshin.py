import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def crear_grafica_mualani():
    """
    Crea una gráfica comparativa de Reloj de Vida vs Maestría Elemental
    para el personaje Mualani de Genshin Impact.
    
    Datos del personaje:
    - Vida Máx.: 33,473
    - Maestría Elemental: 58
    """
    
    # Configurar la figura con un tamaño más grande y fondo
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor('#1a1a2e')
    ax.set_facecolor('#16213e')
    
    # Datos del personaje Mualani
    vida_max = 33473
    maestria_elemental = 58
    
    # Calcular el beneficio de daño estimado para cada stat
    # Para Mualani (DPS Hydro), la Vida Máxima generalmente proporciona más daño
    # que la Maestría Elemental en su estado actual
    beneficio_vida = vida_max * 0.08  # Aprox 8% de conversión de HP a daño para builds HP
    beneficio_maestria = maestria_elemental * 4.5  # Multiplicador estándar de EM para reacciones
    
    categorias = ['Reloj de Vida\n(HP%)', 'Maestría Elemental']
    valores = [beneficio_vida, beneficio_maestria]
    colores = ['#00d4ff', '#ff6b35']  # Azul para HP, Naranja para EM
    
    # Crear barras con gradiente visual
    barras = ax.bar(categorias, valores, color=colores, width=0.6, alpha=0.9)
    
    # Añadir efectos visuales a las barras
    for i, barra in enumerate(barras):
        altura = barra.get_height()
        # Añadir brillo en la parte superior
        rect = patches.Rectangle((barra.get_x(), altura * 0.85), 
                               barra.get_width(), altura * 0.15, 
                               facecolor='white', alpha=0.3)
        ax.add_patch(rect)
        
        # Añadir valores en las barras
        ax.text(barra.get_x() + barra.get_width()/2, altura + max(valores)*0.02,
                f'{valores[i]:.1f}',
                ha='center', va='bottom', fontsize=16, fontweight='bold',
                color='white', 
                bbox=dict(boxstyle='round,pad=0.3', facecolor=colores[i], alpha=0.8))
    
    # Configurar el título principal
    ax.set_title('Comparación de Reloj de Vida vs Maestría Elemental\nPersonaje: Mualani (Genshin Impact)', 
                fontsize=20, fontweight='bold', color='white', pad=30)
    
    # Configurar etiquetas y estilo
    ax.set_ylabel('Beneficio de Daño Estimado', fontsize=14, fontweight='bold', color='white')
    ax.set_xlabel('Tipo de Reliquia Principal', fontsize=14, fontweight='bold', color='white')
    
    # Personalizar los ticks
    ax.tick_params(axis='x', colors='white', labelsize=12)
    ax.tick_params(axis='y', colors='white', labelsize=11)
    
    # Añadir grilla sutil
    ax.grid(True, alpha=0.2, color='white', linestyle='--')
    ax.set_axisbelow(True)
    
    # Añadir información del personaje en un cuadro
    info_texto = f'Stats Actuales de Mualani:\n• Vida Máx.: {vida_max:,}\n• Maestría Elemental: {maestria_elemental}'
    ax.text(0.02, 0.98, info_texto, transform=ax.transAxes, fontsize=11,
            verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', 
            facecolor='#0f3460', alpha=0.9, edgecolor='#00d4ff'),
            color='white')
    
    # Añadir conclusión
    if beneficio_vida > beneficio_maestria:
        conclusion = f'El Reloj de Vida aporta {beneficio_vida/beneficio_maestria:.1f}x más daño\nque la Maestría Elemental'
        color_conclusion = '#00ff88'
    else:
        conclusion = f'La Maestría Elemental aporta {beneficio_maestria/beneficio_vida:.1f}x más daño\nque el Reloj de Vida'
        color_conclusion = '#ff6b35'
    
    ax.text(0.98, 0.02, conclusion, transform=ax.transAxes, fontsize=12,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#2d1b69', 
            alpha=0.9, edgecolor=color_conclusion),
            color=color_conclusion, fontweight='bold')
    
    # Ajustar layout
    plt.tight_layout()
    
    # Guardar la imagen
    nombre_archivo = 'Comparacion_Reloj_Vida_vs_Maestria_Elemental_Mualani.png'
    plt.savefig(nombre_archivo, dpi=300, bbox_inches='tight', 
                facecolor='#1a1a2e', edgecolor='none')
    
    print(f"Gráfica guardada como: {nombre_archivo}")
    return nombre_archivo

def mostrar_stats_mualani():
    """Muestra los stats actuales del personaje Mualani"""
    print("\n=== STATS DE MUALANI (GENSHIN IMPACT) ===")
    print("• Vida Máx.: 33,473")
    print("• Maestría Elemental: 58")
    print("=========================================")

if __name__ == "__main__":
    mostrar_stats_mualani()
    archivo = crear_grafica_mualani()
    print(f"\n✅ Gráfica comparativa creada exitosamente: {archivo}")