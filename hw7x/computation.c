#include "computation.h"
#include "thread_pool.h"
#include <pthread.h>
#include <stdlib.h>
#include <stdio.h>


void thpool_submit_computation(
    struct ThreadPool *pool,
    struct Computation *computation,
    OnComputationComplete on_complete,
    void* on_complete_arg
) {
    computation->task.f = computation->f;
    computation->task.arg = computation->arg;
    pthread_mutex_init(&computation->mutex, NULL);
    pthread_cond_init(&computation->cond_var, NULL);
    computation->finished = false;
    computation->on_complete = on_complete;
    computation->on_complete_arg = on_complete_arg;
    thpool_submit(pool, &computation->task);
}

void thpool_complete_computation(
    struct Computation *computation
) {
    pthread_mutex_lock(&computation->mutex);
    computation->finished = true;
    pthread_cond_signal(&computation->cond_var);
    pthread_mutex_unlock(&computation->mutex);
    if (computation->on_complete) 
        computation->on_complete(computation->on_complete_arg);
}

void thpool_wait_computation(struct Computation *computation){
    pthread_mutex_lock(&computation->mutex);
    while (!computation->finished) {
        pthread_cond_wait(&computation->cond_var, &computation->mutex);
    }
    pthread_mutex_unlock(&computation->mutex);
    pthread_cond_destroy(&computation->cond_var);
    pthread_mutex_destroy(&computation->mutex);
    thpool_wait(&computation->task);
}
