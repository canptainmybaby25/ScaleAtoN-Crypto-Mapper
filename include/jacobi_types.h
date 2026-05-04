// jacobi_types.h

#ifndef JACOBI_TYPES_H
#define JACOBI_TYPES_H

typedef struct {
    double x;
    double y;
} JacobiPoint;

typedef struct {
    int eventId;
    JacobiPoint point;
    // Additional fields can be added as needed
} EventRecord;

#endif // JACOBI_TYPES_H