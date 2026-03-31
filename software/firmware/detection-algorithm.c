/**
 * detection-algorithm.c
 * Algoritmo de deteccion de eventos para Geolocalizador-Encuentrame
 * 
 * Detecta condiciones de impacto, hundimiento, caida o emergencia
 * utilizando sensores y logica de IA embebida.
 */

#include <stdint.h>
#include <stdbool.h>
#include <math.h>

// Configuracion
#define ACCEL_THRESHOLD_IMPACT     8.0f   // g
#define ACCEL_THRESHOLD_FREE_FALL  0.5f   // g
#define PRESSURE_RATE_THRESHOLD    30.0f  // hPa/s
#define VIBRATION_FREQ_THRESHOLD   100.0f // Hz
#define DETECTION_WINDOW_MS        500   // ms
#define CONFIRMATION_SAMPLES       3

// Estados del sistema
typedef enum {
    STATE_ARMED,
    STATE_DETECTING,
    STATE_CONFIRMED,
    STATE_ACTIVATED,
    STATE_SELF_TEST
} system_state_t;

// Estructura de datos de sensores
typedef struct {
    float accel_x, accel_y, accel_z;
    float pressure;
    float temperature;
    float vibration_freq;
    uint32_t timestamp_ms;
} sensor_data_t;

// Variables globales
static system_state_t state = STATE_ARMED;
static uint32_t detection_start_ms = 0;
static uint8_t confirm_count = 0;

// Filtro de media movil para aceleracion
static float accel_moving_avg[10];
static uint8_t accel_idx = 0;

/**
 * Actualiza filtro de media movil
 */
float update_moving_average(float new_value) {
    static float sum = 0.0f;
    static uint8_t count = 0;
    
    sum -= accel_moving_avg[accel_idx];
    accel_moving_avg[accel_idx] = new_value;
    sum += new_value;
    accel_idx = (accel_idx + 1) % 10;
    
    if (count < 10) count++;
    return sum / count;
}

/**
 * Detecta condicion de impacto inminente (aviacion)
 * Basado en aceleracion y patrones de vibracion
 */
bool detect_impending_impact(sensor_data_t *sensor) {
    float accel_mag = sqrtf(sensor->accel_x * sensor->accel_x +
                            sensor->accel_y * sensor->accel_y +
                            sensor->accel_z * sensor->accel_z);
    
    float filtered_accel = update_moving_average(accel_mag);
    
    // Deteccion de caida libre + vibracion anomala
    if (filtered_accel < ACCEL_THRESHOLD_FREE_FALL &&
        sensor->vibration_freq > VIBRATION_FREQ_THRESHOLD) {
        return true;
    }
    
    return false;
}

/**
 * Detecta hundimiento (maritimo)
 * Basado en tasa de cambio de presion
 */
bool detect_sinking(sensor_data_t *sensor) {
    static float last_pressure = 0.0f;
    static uint32_t last_time = 0;
    float pressure_rate;
    
    if (last_time == 0) {
        last_pressure = sensor->pressure;
        last_time = sensor->timestamp_ms;
        return false;
    }
    
    float dt = (sensor->timestamp_ms - last_time) / 1000.0f;
    if (dt > 0) {
        pressure_rate = (sensor->pressure - last_pressure) / dt;
        last_pressure = sensor->pressure;
        last_time = sensor->timestamp_ms;
        
        // Presion aumentando rapidamente (hundimiento)
        if (pressure_rate > PRESSURE_RATE_THRESHOLD) {
            return true;
        }
    }
    
    return false;
}

/**
 * Detecta impacto (terrestre)
 */
bool detect_impact(sensor_data_t *sensor) {
    float accel_mag = sqrtf(sensor->accel_x * sensor->accel_x +
                            sensor->accel_y * sensor->accel_y +
                            sensor->accel_z * sensor->accel_z);
    
    // Impacto repentino de alta G
    if (accel_mag > ACCEL_THRESHOLD_IMPACT) {
        return true;
    }
    
    return false;
}

/**
 * Algoritmo principal de deteccion
 * Retorna true si se debe activar el dispositivo
 */
bool detection_loop(sensor_data_t *sensor, uint8_t scenario) {
    bool event_detected = false;
    
    switch (scenario) {
        case 0: // Aeronautico
            event_detected = detect_impending_impact(sensor);
            break;
        case 1: // Maritimo
            event_detected = detect_sinking(sensor);
            break;
        case 2: // Terrestre
            event_detected = detect_impact(sensor);
            break;
        case 3: // Personal
            // Activacion manual, no automatica
            return false;
        default:
            return false;
    }
    
    // Maquina de estados
    switch (state) {
        case STATE_ARMED:
            if (event_detected) {
                state = STATE_DETECTING;
                detection_start_ms = sensor->timestamp_ms;
                confirm_count = 0;
            }
            break;
            
        case STATE_DETECTING:
            if (event_detected) {
                confirm_count++;
                if (confirm_count >= CONFIRMATION_SAMPLES) {
                    state = STATE_CONFIRMED;
                }
            } else {
                // Reiniciar si no hay confirmacion en la ventana
                if (sensor->timestamp_ms - detection_start_ms > DETECTION_WINDOW_MS) {
                    state = STATE_ARMED;
                }
            }
            break;
            
        case STATE_CONFIRMED:
            // Evento confirmado, activar
            state = STATE_ACTIVATED;
            return true;
            
        default:
            break;
    }
    
    return false;
}

/**
 * Inicializacion del modulo
 */
void detection_init(void) {
    state = STATE_ARMED;
    confirm_count = 0;
    accel_idx = 0;
    for (int i = 0; i < 10; i++) {
        accel_moving_avg[i] = 0.0f;
    }
}

/**
 * Autoprueba (self-test)
 */
bool detection_self_test(void) {
    state = STATE_SELF_TEST;
    
    // Simular condiciones de prueba
    sensor_data_t test_sensor;
    test_sensor.accel_x = 0.1f;
    test_sensor.accel_y = 0.1f;
    test_sensor.accel_z = 0.3f;
    test_sensor.pressure = 1013.25f;
    test_sensor.vibration_freq = 150.0f;
    test_sensor.timestamp_ms = 1000;
    
    bool result = detection_loop(&test_sensor, 0);
    
    state = STATE_ARMED;
    return result; // Deberia retornar true si funciona
}
