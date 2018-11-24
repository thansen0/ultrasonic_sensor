//
//  ViewController.swift
//  MicrophoneAnalysis
//
//  Created by Kanstantsin Linou, revision history on Githbub.
//  Copyright © 2018 AudioKit. All rights reserved.
//

import AudioKit
import AudioKitUI
import Cocoa
//import AudioKitPlaygrounds

class ViewController: NSViewController {

    @IBOutlet private var frequencyLabel: NSTextField!
    @IBOutlet private var amplitudeLabel: NSTextField!
//    @IBOutlet private var noteNameWithSharpsLabel: NSTextField!
//    @IBOutlet private var noteNameWithFlatsLabel: NSTextField!
    @IBOutlet private var audioInputPlot: EZAudioPlot!
//    @IBOutlet private var messageLabel: NSTextField!

    var mic: AKMicrophone!
    var tracker: AKFrequencyTracker!
    var silence: AKBooster!
    var counter = 0
    let noteFrequencies = [16.35, 17.32, 18.35, 19.45, 20.6, 21.83, 23.12, 24.5, 25.96, 27.5, 29.14, 30.87]
    
    func setupPlot() {
        let plot = AKNodeOutputPlot(mic, frame: audioInputPlot.bounds)
//        let fft = AKFFTTap(mic)
//        let plot = AKNodeFFTPlot(mic, frame: audioInputPlot.bounds)
        plot.plotType = .rolling
        plot.shouldFill = true
        plot.shouldMirror = true
        plot.color = NSColor.blue
        plot.autoresizingMask = NSView.AutoresizingMask.width
        audioInputPlot.addSubview(plot)
//        audioInputPlot.addSubview(plot2)
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        AKSettings.audioInputEnabled = true
        mic = AKMicrophone()
        tracker = AKFrequencyTracker(mic)
        silence = AKBooster(tracker, gain: 0)
    }

    override func viewDidAppear() {
        super.viewDidAppear()
        AudioKit.output = silence
        do {
            try AudioKit.start()
        } catch {
            AKLog("AudioKit did not start!")
        }
        setupPlot()
        Timer.scheduledTimer(timeInterval: 1,
                             target: self,
                             selector: #selector(ViewController.updateUI),
                             userInfo: nil,
                             repeats: true)
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }

    @objc func updateUI() {
        if tracker.amplitude > 0.1 {
            
            frequencyLabel.stringValue = String(format: "%0.1f", tracker.frequency)

            var frequency = Float(tracker.frequency)
            while frequency > Float(noteFrequencies[noteFrequencies.count - 1]) {
                frequency /= 2.0
            }
            while frequency < Float(noteFrequencies[0]) {
                frequency *= 2.0
            }
            if(tracker.frequency >= 14500 && tracker.frequency <= 15499) {
                counter+=1
                print(0, terminator:" ")
            }
            if(tracker.frequency >= 15500 && tracker.frequency <= 17500) {
                counter+=1
                print(1, terminator:" ")
            }
            if(counter == 14){
                print()
                counter = 0
            }
            var minDistance: Float = 10_000.0
            var index = 0

            for i in 0..<noteFrequencies.count {
                let distance = fabsf(Float(noteFrequencies[i]) - frequency)
                if distance < minDistance {
                    index = i
                    minDistance = distance
                }
            }

        }
        
        amplitudeLabel.stringValue = String(format: "%0.2f", tracker.amplitude)
    }
}