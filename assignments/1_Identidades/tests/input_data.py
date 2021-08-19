# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["1", "180"],
            ["Opcion:", "Grados:", "1.0"],
            "Revisa el código de la función secante_cuadrada",
        ),
        # Test case 2
        (
            ["2", "135"],
            ["Opcion:", "Grados:", "-1.0"],
            "Revisa el código de la función cotangente",
        ),
        # Test case 3
        (
            ["3"],
            ["Opcion:", "Adios"],
            "Revisa tu mensaje para salir: Adios",
        ),
        # Test case 4
        (
            ["-4"],
            ["Opcion:", "Opcion_invalida"],
            "Revisa tu mensaje de Opcion_invalida",
        ),
    ]
