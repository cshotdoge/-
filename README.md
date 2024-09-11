
# King of Glory Esports Competition Simulation

This project simulates different tournament formats for the King of Glory (王者荣耀) esports competition. The script models results of various tournament styles including Swiss format, single round-robin, and knockout stages to estimate team performance and progression.

## Features

- **Swiss Tournament Simulation**: Simulates a Swiss-system tournament, tracking team performance through multiple rounds.
- **BO3 and BO7 Knockout Matches**: Models best-of-three (BO3) and best-of-seven (BO7) matches to determine advancing teams.
- **Performance Tracking**: Records team performance across different tournament stages (e.g., quarter-finals, semi-finals, finals).
- **Result Export**: Outputs simulation results to an Excel file, including probabilities of teams reaching various stages.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/kog-esports-simulation.git
    ```

2. Install the required packages:

    ```bash
    pip install pandas
    ```

## Usage

1. Run the script:

    ```bash
    python tournament_simulation.py
    ```

2. Input the number of simulation runs when prompted. The script will run the tournament simulation based on the input and display results such as the probability of teams advancing through different stages.

3. The final results are exported to an Excel file (`final15.0.xlsx`), summarizing team probabilities for each tournament stage.

## Tournament Formats

### 1. **Swiss System**
   - Teams compete in multiple rounds.
   - After each round, teams with similar scores face off.
   - The top-performing teams advance to knockout stages.

### 2. **BO3 Single Round Robin**
   - Teams play BO3 matches against each other.
   - The results are used to determine rankings for the knockout stage.

### 3. **Knockout Stage (BO7)**
   - Teams compete in best-of-seven matches in quarter-finals, semi-finals, and finals.
   - The winner of the finals is crowned the champion.

### 4. **Shiguan Format**
   - A fixed group-based format that randomly assigns teams into groups and progresses them to knockout stages based on performance.

## Example Output

The results show the probability of each team reaching various stages:

| Team   | Sw 8   | Sw 4   | Sw 2   | Sw Championship | Bo 8  | Bo 4  | ... | SG 8   | SG Championship |
|--------|--------|--------|--------|-----------------|-------|-------|-----|--------|-----------------|
| Team 1 | 0.75   | 0.5    | 0.25   | 0.1             | 0.8   | 0.4   | ... | 0.65   | 0.15            |
| Team 2 | 0.6    | 0.45   | 0.35   | 0.2             | 0.7   | 0.5   | ... | 0.7    | 0.2             |

## License

This project is licensed under the MIT License.

## Contributions

Feel free to open issues or submit pull requests to improve the simulation model or extend functionality to other esports competitions.

