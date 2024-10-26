package com.meteortracker.service;

import org.springframework.stereotype.Service;
import java.io.BufferedReader;
import java.io.InputStreamReader;

@Service
public class TrackerService {

    // Method to fetch meteor data by name within a date range
    public String fetchMeteorByName(String name, String startDate, String endDate) {
        return runPythonScript("name", name, startDate, endDate);
    }

    // Method to fetch meteor data by date range
    public String fetchMeteorsByDate(String startDate, String endDate) {
        return runPythonScript("date", startDate, endDate);
    }

    // Method to fetch meteor data by NEO reference ID
    public String fetchMeteorById(String neoId) {
        return runPythonScript("id", neoId);
    }

    // General method to run the Python script with dynamic arguments
    private String runPythonScript(String... args) {
        try {
            // Prepare the command with "python3", script path, and additional arguments
            String[] command = new String[args.length + 2];
            command[0] = "python3";
            command[1] = "scripts/fetch_meteor_data.py"; 
            System.arraycopy(args, 0, command, 2, args.length);

            ProcessBuilder processBuilder = new ProcessBuilder(command);
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder output = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line);
            }

            return output.toString(); // Return the JSON output from the Python script

        } catch (Exception e) {
            e.printStackTrace();
            return "Error fetching data: " + e.getMessage();
        }
    }
}
