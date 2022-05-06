
## Homework: Task 1

// redLight
var redLight = new Sphere(
    new Vector3(0, -1, -10), // center
    .5, // radius
    new Material(
        new Vector3(1.0, 0.0, 0.0), // color
        0, // reflection
        0,  // transparency
        new Vector3() // emissionColor (lights only)
    )
);

// yellowLight
var yellowLight = new Sphere(
    new Vector3(0,  0, -10), // center
    .5, // radius
    new Material(
        new Vector3(1.0, 1.0, 0.0), // color
        0, // reflection
        0,  // transparency
        new Vector3() // emissionColor (lights only)
    )
);

// greenLight
var greenLight = new Sphere(
    new Vector3(0, 1, -10), // center
    .5, // radius
    new Material(
        new Vector3(0.0, 1.0, 0.0), // color
        0, // reflection
        0,  // transparency
        new Vector3() // emissionColor (lights only)
    )
);



## Homework: Task 2

// back light
var light2 = new Sphere(
    new Vector3(30, 30, 0), // center
    1, // radius
    new Material(
        new Vector3(), // color
        0, // reflection
        0, // transparency
        new Vector3(1, 1, 1)
    )
);

// redLight2
var redLight2 = new Sphere(
    new Vector3(2, 0, -10), // center
    .5, // radius
    new Material(
        new Vector3(1.0, 0.0, 0.0), // color
        0, // reflection
        0,  // transparency
        new Vector3() // emissionColor (lights only)
    )
);

// yellowLight2
var yellowLight2 = new Sphere(
    new Vector3(2,  1, -10), // center
    .5, // radius
    new Material(
        new Vector3(1.0, 1.0, 0.0), // color
        0, // reflection
        0,  // transparency
        new Vector3() // emissionColor (lights only)
    )
);

// greenLight2
var greenLight2 = new Sphere(
    new Vector3(2, 2, -10), // center
    .5, // radius
    new Material(
        new Vector3(0.0, 1.0, 0.0), // color
        0, // reflection
        0,  // transparency
        new Vector3() // emissionColor (lights only)
    )
);
