package com.meteortracker.controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import com.meteortracker.service.TrackerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;


@RestController
@CrossOrigin(origins = "http://127.0.0.1:5500") 
@RequestMapping("/api/trackers") // Base URL for all endpoints in this controller
public class TrackerController {

    
    
    @Autowired // Automatically injects the TrackerService instance
    private TrackerService trackerService;

    // Endpoint for searching by name within a date range
    @PostMapping("/searchByName")
    public String getMeteorByName(@RequestParam String name,
                                  @RequestParam String startDate,
                                  @RequestParam String endDate) {
        return trackerService.fetchMeteorByName(name, startDate, endDate);
    }

    // Endpoint for searching by date range
    @PostMapping("/searchByDate")
    public String getMeteorsByDate(@RequestParam String startDate,
                                   @RequestParam String endDate) {
        return trackerService.fetchMeteorsByDate(startDate, endDate);
    }

    // Endpoint for searching by NEO reference ID
    @PostMapping("/searchById")
    public String getMeteorById(@RequestParam String neoId) {
        return trackerService.fetchMeteorById(neoId);
    }

   
}
