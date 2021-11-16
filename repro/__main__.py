import modin.pandas as pd
import pandera as pa
import pandera.typing as P


class Example(pa.SchemaModel):
    strings: P.Index[P.STRING]

    class Config:
        coerce = True


@pa.decorators.check_types()
def main() -> P.DataFrame[Example]:
    return pd.DataFrame(
        index=[
            "should",
            "not",
            "throw",
            "during",
            "schema",
            "validate",
        ],
    )


if __name__ == "__main__":
    main()
