--------------------------------Multithreading-------------------------------


¿Por qué usamos ThreadPoolExecutor?
ThreadPoolExecutors proporciona una abstracción simple en torno a la creación de varios subprocesos y el uso de estos subprocesos para realizar tareas de manera simultánea.

¿Qué son los max_workers?
Lo que normalmente significa es el número de subproceso(hilos) que tendra.

Tiempo con Multithreading:0.0010013580322265625 s


--------------------------------Multiprocessing-------------------------------


¿Por qué usamos multiprocessing?
Se utiliza cuando se requiere paralelismo basado en funciones, donde podría definir diferentes funcionalidades con parámetros que reciben y ejecutar esas diferentes funciones en paralelo que están haciendo cálculos totalmente diferentes.

¿Qué es una pool?
Ofrece un medio conveniente para paralelizar la ejecución de una función a través de múltiples valores de entrada, distribuyendo los datos de entrada a través de procesos, es decir, paralelismo basado en datos.

Tiempo con Multiprocessing: 0.07910728454589844s


--------------------------------Sincrono-------------------------------

Tiempo con Sincrono: 7.296548400000001s