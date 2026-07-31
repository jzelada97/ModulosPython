from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10, description='Station identifier')
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


def main() -> None:
    print('Space Station Data Validation')
    print('========================================')
    try:
        valid = SpaceStation(
            station_id='ISS001',
            name='International Space Station',
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance='2024-01-01T12:00:00',  # type: ignore[arg-type]
            is_operational=True,
            notes='All systems nominal.'
        )
        print('Valid station created:')
        print(f'ID: {valid.station_id}')
        print(f'Name: {valid.name}')
        print(f'Crew: {valid.crew_size} people')
        print(f'Power: {valid.power_level}%')
        print(f'Oxygen: {valid.oxygen_level}%')
        print(f"Status: {'Operational' if valid.is_operational else 'Non-operational'}")
    except ValidationError as e:
        print('Unexpected validation error creating valid instance:')
        print(e)

    print('========================================')
    print('Expected validation error:')
    try:
        SpaceStation(
            station_id='ST',  # too short
            name='Tiny Station',
            crew_size=25,  # too many
            power_level=120.0,  # out of range
            oxygen_level=-5.0,
            last_maintenance='not a datetime',  # type: ignore[arg-type]
            notes=None
        )
    except ValidationError as e:
        print(e)


if __name__ == '__main__':
    main()
